from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):
    left_column = ColumnBlock(icon='arrow-left', label='Left column content')
    right_column = ColumnBlock(icon='arrow-right', lable='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

class VideoBlock(blocks.StructBlock):
    """Only used for Video Card modals."""
    video = EmbedBlock() # <-- the part we need

    class Meta:
        template = "streams/video_card_block.html"
        icon = "media"
        label = "Embed Video"


