from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from info.mixins import ImageDisplayAminMixin
from info.models import MainInfo, HomePageImage, SocialMedia, Service, AboutUs, Event, ContactUs


class HomePageImageeInlineAdmin(ImageDisplayAminMixin, admin.TabularInline):
    model = HomePageImage
    readonly_fields = ('create_at', 'update_at')
    readonly_image_fields = ['view_image']


class SocialMediaInlineAdmin(admin.TabularInline):
    model = SocialMedia
    readonly_fields = ('create_at', 'update_at')


class MainInfoAdmin(ImageDisplayAminMixin, TranslationAdmin):
    list_display = ['__str__', 'create_at', 'update_at']
    readonly_fields = ['create_at', 'update_at']
    search_fields = ['title', 'description']
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'image', 'view_image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )
    inlines = [SocialMediaInlineAdmin, HomePageImageeInlineAdmin]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class ActiveTitleWithDescriptionAdmin(ImageDisplayAminMixin, TranslationAdmin):
    list_display = ['__str__', 'create_at', 'update_at']
    list_filter = ['is_active']
    readonly_fields = ['create_at', 'update_at']
    search_fields = ['title', 'description']
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'image', 'view_image', 'is_active')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class EventAdmin(ImageDisplayAminMixin, TranslationAdmin):
    list_display = ['title', 'is_active', 'create_at', 'update_at']
    list_filter = ['is_active']
    readonly_fields = ['create_at', 'update_at']
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'is_active')}),
        (_('More Info'), {'fields': ('start_time', 'end_time', 'location', 'image', 'view_image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_at', 'update_at')
    search_fields = ('email', 'full_name', 'message')
    readonly_fields = ['create_at', 'update_at']
    fieldsets = (
        (_('Main Info'), {'fields': ('full_name', 'email', 'phone_number', 'message')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(Service, ActiveTitleWithDescriptionAdmin)
admin.site.register(AboutUs, ActiveTitleWithDescriptionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
