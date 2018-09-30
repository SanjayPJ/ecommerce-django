from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(null=True, blank=True)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image = models.ImageField(upload_to='products/', null=True, blank=True)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)