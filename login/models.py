from django.db import models

# Create your models here.
class users(models.Model):
    '''用户表'''

    uid = models.CharField()
    name = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'