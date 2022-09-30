from django.db import models
from django.conf import settings


class Product(models.Model):
    CHROM = models.CharField(
        max_length=50, null=False, blank=False
    )
    POS = models.CharField(
        max_length=50,null=False, blank=False
    )
    ID_vcf = models.CharField(max_length=50, null=False, blank=False)
    REF = models.CharField(
        max_length=50,null=False, blank=False
    )
    ALT = models.CharField(
        max_length=50,null=False, blank=False
    )