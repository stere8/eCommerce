from products.models import category

def categories(request):
    return {
        'categories' : category.objects.all()
    }