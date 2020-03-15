from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

        
class Article(models.Model):
    CATEGORY_CHOICES = (
        ('Technology','Technology'),
        ('Hardware','Hardware'),
        ('Software','Software'),
        ('communication','Communication'),
    )
    
    image = models.FileField(default='')
    image2 = models.FileField(default='')
    title =  models.CharField(max_length=2000,default='')
    slug = models.SlugField(default='')
    author =  models.CharField(max_length=2000,default='')
    text = models.TextField(default='')
    text2 = models.TextField(default='')
    quote = models.CharField(max_length=2000,default='')
    quote_name = models.CharField(max_length=2000,default='')
    l_heading = models.CharField(max_length=2000,default='')
    l_heading_text = models.TextField(max_length=2000,default='')
    s_heading = models.CharField(max_length=2000,default='')
    s_heading_text = models.TextField(max_length=2000,default='')
    category = models.CharField(max_length=2000, choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(default='')
    tag_1 = models.CharField(max_length=2000,default='')
    tag_2 = models.CharField(max_length=2000,default='')
    tag_3 = models.CharField(max_length=2000,default='')
    id = models.int(max_length=2000,default='')

    class Meta:
        ordering = ['-created_date']



    def __str_(self):
      return self.title

    def get_absolute_url(self):
     return reverse('post_detail', )
      
  


    
   