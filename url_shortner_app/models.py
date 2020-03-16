from django.db import models


class ShortURL(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    actual_url = models.URLField(max_length=500,
                                 primary_key=True)
    short_url = models.CharField(max_length=50)


class AccessedTime(models.Model):
    short_URL = models.ForeignKey('ShortURL',
                                  related_name='short_URL',
                                  on_delete=models.CASCADE)
    accessed = models.DateTimeField(auto_now_add=True)
