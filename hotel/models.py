from django.db import models

class Hotel(models.Model):

    class Meta:
        db_table = 'hotel_table'
        verbose_name = 'hotel'
        verbose_name_plural = 'hotels'
        ordering = ['-id']
