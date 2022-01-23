from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,null=False,editable=False, db_index=True)

    def __str__(self):
        return self.name
    
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = RichTextField()
    image = models.ImageField(upload_to='posts')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, db_index=True, null=False, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str_(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

