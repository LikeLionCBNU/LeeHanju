from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    img = models.ImageField(blank=True)
    tags = TaggableManager(blank=True)
    hits = models.PositiveIntegerField(default= 0)
        
    def __str__(self):
        return self.title
    
    @property
    def update_hits(self):
        self.hits = self.hits + 1
        self.save()