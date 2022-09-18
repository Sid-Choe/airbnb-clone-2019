from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_KOREAN = "korean"
    LANGUAGE_ENGLISH = "english"

    LANGUAGE_CHOICES = ((LANGUAGE_KOREAN, "korean"),
                        (LANGUAGE_ENGLISH, "english"))

    CURRENCY_KRW = "krw"
    CURRENCY_USD = "usd"

    CURRENCY_CHOICES = ((CURRENCY_KRW, "krw"), (CURRENCY_USD, "usd"))

    avatar = models.ImageField(blank=True, upload_to="avatar")
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=7,
                                choices=LANGUAGE_CHOICES, blank=True)
    currency = models.CharField(max_length=3,
                                choices=CURRENCY_CHOICES, blank=True)
    super_host = models.BooleanField(default=False)
