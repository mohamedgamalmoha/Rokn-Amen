from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from info.constants import DEFAULT_PRODUCT_IMAGE_URL


class ImageDisplayAminMixin:
    image_field_name = 'image'
    readonly_image_fields = ['list_image', 'view_image']

    def _show_image(self, obj, width=150, height=200):
        image = self.get_image_field(obj)
        if image and image.url:
            return mark_safe(f"<a href='{image.url}' ><img src='{image.url}' width={width} height={height}></a>")
        return mark_safe(f"<a href='#' ><img src='{DEFAULT_PRODUCT_IMAGE_URL}' width={width} height={height}></a>")

    def get_image_field(self, obj):
        return getattr(obj, self.image_field_name, None)

    def list_image(self, obj=None):
        if obj is None:
            return ''
        return self._show_image(obj, width=75, height=50)

    def view_image(self, obj=None):
        if obj is None:
            return ''
        return self._show_image(obj, width=150, height=200)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if isinstance(readonly_fields, (tuple, list)):
            readonly_fields = [*readonly_fields, *self.readonly_image_fields]
        return readonly_fields

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if isinstance(list_display, (tuple, list)) and 'list_image' not in list_display:
            list_display = [*list_display, 'list_image']
        return list_display

    list_image.short_description = _('Thumbnail')
    view_image.short_description = _('Image')
