from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
  name = models.CharField(max_length=128, unique=True)
  views = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  slug = models.SlugField(default='')

  def save(self, *args, **kwargs):
    # prevents slug from changing every time name changes
    if self.id is None:
      self.slug = slugify(self.name)
    # self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)

  def __str__(self):
    return self.name
  # changing the pluralization and adding an ordering
  class Meta:
    ordering = ["name"]
    verbose_name_plural = "categories"
  
  def popular(self):
    return self.likes >= 100
  popular.short_description = 'Top Category?'

class Page(models.Model):
  category = models.ForeignKey(Category)
  title = models.CharField(max_length=128)
  url = models.URLField()
  views = models.IntegerField(default=0)


  def __str__(self):
    return '%s id: %s' % (self.title, self.id)
