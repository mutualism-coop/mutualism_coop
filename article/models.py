from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ArticlePage(Page):
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
    ]
