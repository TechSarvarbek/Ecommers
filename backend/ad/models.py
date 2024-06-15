from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='ad_images/',  null=True, blank=True)

    def __str__(self):
        return self.title