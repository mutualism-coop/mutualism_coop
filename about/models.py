from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class AboutPage(Page):
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("content", classname="full"),
    ]
