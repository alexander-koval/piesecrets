from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width card-img', "width-592"))

unregister_image_format('left')
register_image_format(Format('left', 'Left-aligned', 'richtext-image left card-img', 'width-500'))

unregister_image_format('right')
register_image_format(Format('right', 'Right-aligned', 'richtext-image right card-img', 'width-500'))

# class CardImageFormat(Format):

#     def image_to_html(self, image, alt_text, extra_attributes=None):
#         custom_html = super().image_to_html(image, alt_text, extra_attributes)
#         return custom_html



# register_image_format(
#     CardImageFormat('card_fullwidth', 'Full width Card Image', 'card-img', 'width-750')
# )