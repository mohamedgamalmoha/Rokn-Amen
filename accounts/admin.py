from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.backends import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_time', 'content_type', 'object_repr', 'action_flag', 'change_message')
    search_fields = ('object_repr', 'change_message', 'user__username')
    list_filter = ('action_flag', )
    readonly_fields = ('action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag',
                       'change_message')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_("Personal Info"), {"fields": ("username", "full_name", "phone_number", "email", "gender", "birth_date",
                                         "national_id", "password")}),
        (_("Education"), {"fields": ("education_level", "specialization")}),
        (_("Work Info"), {"fields": ("jop_title", "work_place", "department")}),
        (_("Address Info"), {"fields": ("conservative", "state", "region", "address")}),
        (_("Extra"), {"fields": ("skills", "ready_to_join", "recommendations")}),
        (_("Permissions"), {"fields": ("is_active",  "is_staff", "is_superuser", "user_permissions")}),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("-date_joined",)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
