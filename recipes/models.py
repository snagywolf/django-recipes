from django.db import models
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeModels(models.Model):
    title = models.CharField(
        max_length=100
    )
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    description = models.TextField()

    image = models.ImageField(
        upload_to='recipes/images/'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
