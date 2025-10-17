from django.db import models
from django.utils.translation import gettext_lazy as _

from info.enums import SocialMediaPlatform


class MainInfo(models.Model):
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(null=True, blank=True, upload_to='home/', verbose_name=_("Image"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _('Website Main Info')
        verbose_name_plural = _('Website Main Info')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class SocialMedia(models.Model):
    info = models.ForeignKey(MainInfo, null=True, on_delete=models.CASCADE, related_name="social_media_links",
                                   verbose_name=_("Website Main Info"))
    platform = models.CharField(max_length=20, choices=SocialMediaPlatform.choices, verbose_name=_("Platform"))
    url = models.CharField(max_length=250, null=True, verbose_name=_("Link / Phone Number"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.url)


class HomePageImage(models.Model):
    info = models.ForeignKey(MainInfo, default=None, on_delete=models.CASCADE, related_name="header_images",
                                   verbose_name=_("Website Main Info"))
    image = models.ImageField(null=True, blank=True, upload_to='headers/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"),
                                    help_text=_("Setting it to false, makes the image disappear from the page"))
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name=_('Order By'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    class Meta:
        verbose_name = _('Home Page Image')
        verbose_name_plural = _('Home Page Images')
        ordering = ('order', '-create_at', '-update_at')


class Service(models.Model):
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(null=True, upload_to='services/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class AboutUs(models.Model):
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(null=True, upload_to='about_us/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(blank=True, verbose_name= _("Description"))
    start_time = models.DateTimeField(null=True, blank=True, verbose_name=_("Start Time"))
    end_time = models.DateTimeField(null=True, blank=True, verbose_name=_("End Time"))
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Location"))
    image = models.ImageField(blank=True, null=True, upload_to='events/', verbose_name=_("Event Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class ContactUs(models.Model):
    full_name = models.CharField(max_length=120, null=True, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(max_length=11, null=True, verbose_name=_("Phone Number"))
    message = models.TextField(verbose_name=_("Message"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.full_name)
