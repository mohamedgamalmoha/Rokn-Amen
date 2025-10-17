from django.db import models
from django.utils.translation import gettext_lazy as _


class SocialMediaPlatform(models.TextChoices):
    FACEBOOK = 'facebook', _("Facebook")
    TWITTER = 'twitter', _("Twitter")
    INSTAGRAM = 'instagram', _("Instagram")
    INSTAGRAM_2 = 'instagram_2', _("Instagram 2")
    LINKEDIN = 'linkedin', _("LinkedIn")
    TIKTOK = 'tiktok', _("TikTok")
    YOUTUBE = 'youtube', _("YouTube")
    WAZE = 'waze', _("Waze")
    PHONE_NUMBER_1 = 'phone_number_1', _('Phone Number 1')
    PHONE_NUMBER_2 = 'phone_number_2', _('Phone Number 2')
