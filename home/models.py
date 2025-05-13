# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Client(models.Model):

    #__Client_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Clienttype(models.Model):

    #__Clienttype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Clienttype_FIELDS__END

    class Meta:
        verbose_name        = _("Clienttype")
        verbose_name_plural = _("Clienttype")


class Payment(models.Model):

    #__Payment_FIELDS__
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)

    #__Payment_FIELDS__END

    class Meta:
        verbose_name        = _("Payment")
        verbose_name_plural = _("Payment")



#__MODELS__END
