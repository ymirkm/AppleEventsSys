from django.db import models

class Imagen(models.Model):
	kind = models.CharField(max_length=20, blank=False, null=False)
	number = models.CharField(max_length=7, blank=False, null=False)
