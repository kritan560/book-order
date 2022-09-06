from django.shortcuts import render, redirect
from book.models import Book
from .models import Comment
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# @login_required
def make_comment(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        comment = request.POST['comment']
        Comment.objects.create(user=get_user(request), comment_on=book, comment=comment )
        return redirect('book-detail', pk)

    else:
        comment = Comment.objects.all()
        context = {'comment':comment}
        return render(request, 'book/detail-book/detail-book.html', context)
        
class DetailBook(LoginRequiredMixin, View):
    def get(self, request ,pk):
        # print(dir(request.user))
        # print(request.user.is_staff)
        model = Book.objects.get(id=pk)
        comment = Comment.objects.filter(comment_on=model)
        context = {'comment':comment, 'book':model}
        return render(request, 'comment/comment-book.html', context)