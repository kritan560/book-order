from django.db import models
from author.models import Author
from category.models import Category

# Create your models here.
class Book(models.Model):
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField()
    page_num = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book/image')
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def authors(self):
        return [author for author in self.author.all()]

    def categorys(self):
        return [category for category in self.category.all()]
        