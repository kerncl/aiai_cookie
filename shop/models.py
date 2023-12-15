import uuid

from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products')

    class Meta:
        ordering = ['-updated', 'available','name']

    def image_tag(self):
        return mark_safe(f"<img src='{self.image.url}' width='150' height='150' />")

    image_tag.short_description = 'Image'

    def save(self, *args, **kwargs):
        if self.image.storage.exists(self.image.name):
            # if same name image submitted
            self.image.name = self.image.name + '_' + uuid.uuid4()[:8]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product', args=[self.slug])

    def __str__(self):
        return self.name
