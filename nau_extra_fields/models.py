"""
Database models for nau_extra_fields.
"""

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class NauUserExtendedModel(models.Model):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    data_authorization = models.BooleanField(
        verbose_name=_(
            "I have read and understood the <a href='https://www.nau.edu.pt/legal/politica-de-privacidade/'"
            " rel='noopener' target='_blank'>Privacy Policy</a>"
        )
    )

    nickname = models.CharField(
        blank=True,
        max_length=255,
        validators=[MinLengthValidator(2)],
        verbose_name=_("Nickname"),
    )

    bio = models.TextField(
        blank=True,
        verbose_name=_("Biography"),
        help_text=_("Tell us a bit about yourself."),
    )

    wants_newsletter = models.BooleanField(
        default=False,
        verbose_name=_("Subscribe to newsletter"),
    )

    favorite_language = models.CharField(
        blank=True,
        max_length=50,
        choices=[
            ("python", "Python"),
            ("javascript", "JavaScript"),
            ("java", "Java"),
            ("go", "Go"),
        ],
        verbose_name=_("Favorite programming language"),
    )

    password_hint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Password hint"),
        help_text=_("Optional hint to remember your password."),
    )

    terms_accepted = models.BooleanField(
        default=False,
        verbose_name=_("I accept the Terms and Conditions."),
    )

    registration_token = models.CharField(
        blank=True,
        max_length=64,
        editable=False,
        verbose_name=_("Registration token (internal)"),
    )

    class Meta:
        verbose_name = _("Extra Info")
        verbose_name_plural = _("Extra Info entries")

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<NauUserExtendedModel, ID: {self.id}, User: {self.user.username}>"
