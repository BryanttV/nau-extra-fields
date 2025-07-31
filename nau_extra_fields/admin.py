"""
Admin configuration for nau_extra_fields models.
"""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import NauUserExtendedModel


@admin.register(NauUserExtendedModel)
class NauUserExtendedModelAdmin(admin.ModelAdmin):
    """
    Admin configuration for NauUserExtendedModel.
    """

    list_display = (
        "id",
        "user_username",
        "nickname",
        "data_authorization",
        "wants_newsletter",
        "terms_accepted",
        "favorite_language",
    )

    list_filter = (
        "data_authorization",
        "wants_newsletter",
        "terms_accepted",
        "favorite_language",
    )

    search_fields = (
        "user__username",
        "user__email",
        "nickname",
    )

    readonly_fields = ("registration_token",)

    fieldsets = (
        (_("User Information"), {"fields": ("user", "nickname", "bio")}),
        (_("Preferences"), {"fields": ("favorite_language", "wants_newsletter")}),
        (_("Authorizations"), {"fields": ("data_authorization", "terms_accepted")}),
        (_("Security"), {"fields": ("password_hint", "registration_token"), "classes": ("collapse",)}),
    )

    def user_username(self, obj):
        """
        Display the username of the related user.
        """
        if obj.user:
            return obj.user.username
        return _("No user")

    user_username.short_description = _("Username")
    user_username.admin_order_field = "user__username"
