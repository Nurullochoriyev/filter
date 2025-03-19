from django.db import models

# Create your models here.
from django.db import models

from  django.contrib import *
class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# class bezuser(models.Model)




class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='news')
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name="get_news")
    video = models.FileField(upload_to='video/',null=True,blank=True)
    is_bool = models.BooleanField(default=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NEW"
        verbose_name_plural = "NEWS"
        ordering = ['-created_ed']

