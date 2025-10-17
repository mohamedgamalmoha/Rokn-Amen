from django.db import models
from django.utils.translation import gettext_lazy as _


class EducationLevel(models.TextChoices):
    HIGH_SCHOOL = 'HS', _('High School')
    DIPLOMA = 'DP', _('Diploma')
    BACHELOR = 'BA', _('Bachelor')
    MASTER = 'MA', _('Master')
    DOCTORATE = 'PhD', _('Doctorate')


class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
