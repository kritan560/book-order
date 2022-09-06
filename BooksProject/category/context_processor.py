from .models import Category

def all_category(request):
    category = Category.objects.all()
    context = {'category':category}
    return context