from .models import Category

def menu_categories(request):
    categories = Category.objects.filter(parent=None, is_featured = False)

    return {'menu_categories': categories}


def menu_tags(request):
    tags = Category.objects.filter(is_featured = True)

    return {'menu_tags': tags}
