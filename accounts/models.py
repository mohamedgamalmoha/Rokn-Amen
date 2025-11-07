from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.enums import Gender
from accounts.enums import EducationLevel


class User(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True, verbose_name=_("Employee ID"))
    full_name = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("Full Name"))
    gender = models.CharField(max_length=4, choices=Gender.choices, default=Gender.MALE, verbose_name=_("Gender"))

    jop_title = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Jop Title"))
    work_place = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Work Place"))
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Department"))

    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Phone Number"))
    national_id = models.CharField(max_length=25, blank=True, null=True, verbose_name=_("National ID"))

    education_level = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=EducationLevel.choices,
        default=EducationLevel.HIGH_SCHOOL,
        verbose_name=_("Education"),
    )
    specialization = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Specialization"),
        help_text=_("e.g. Computer Science, Business Administration, Engineering"),
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("Birth Date"))

    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("City"))
    branch = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Branch"))
    conservative = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Conservative"))
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("State"))
    region = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Region"))
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Address"))

    skills = models.TextField(blank=True, null=True, verbose_name=_("Skills"))
    ready_to_join = models.BooleanField(default=False, verbose_name=_("Ready to Join"))
    recommendations = models.TextField(blank=True, null=True, verbose_name=_("Recommendations"))

    first_name = None
    last_name = None

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def __str__(self) -> str:
        return str(self.full_name)
