from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=128, unique=True)

  def __str__(self):
    return "%s id: %s" % (self.name, self.id)
  # changing the pluralization and adding an ordering
  class Meta:
    ordering = ["name"]
    verbose_name_plural = "categories"

class Page(models.Model):
  category = models.ForeignKey(Category)
  title = models.CharField(max_length=128)
  url = models.URLField()
  views = models.IntegerField(default=0)

  def __str__(self):
    return '%s id: %s' % (self.title, self.id)
