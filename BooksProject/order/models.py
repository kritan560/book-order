from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    status_choices = [
        ('pending','Pending'),
        ('reject','Reject'),
        ('completed','Completed'),
        ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=status_choices, default='pending')
    num_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.book)