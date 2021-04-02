from django.db import models

from wagtail.core.models import Page, TranslatableMixin
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


@register_snippet
class Author(TranslatableMixin, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ArticlePage(Page):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=False, null=True,
    )
    content = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="article_pages",
    )

    content_panels = Page.content_panels + [
        FieldPanel("content", classname="full"),
        ImageChooserPanel("image"),
        SnippetChooserPanel("author"),
    ]
