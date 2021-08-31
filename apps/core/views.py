from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from apps.store.models import Product, Category, Brand, ProductAttribute
from django.db.models import Max,Min,Count,Avg
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def frontpage(request):
    products = Product.objects.filter(is_featured=True).order_by('-id')[:8]
    featured_categories = Category.objects.filter(is_featured=True).order_by('-id')

    context = {
        'products': products,
        'featured_categories': featured_categories,
    }

    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def brand(request):
    data = Brand.objects.all()

    context = {'data': data}
    return render(request, 'parts/brand.html', context)


# Filter Data
# Filter Data
def filter_data(request):
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	brands=request.GET.getlist('brand[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	allProducts=Product.objects.all().order_by('-id').distinct()
	allProducts=allProducts.filter(productattribute__price__gte=minPrice)
	allProducts=allProducts.filter(productattribute__price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(productattribute__color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(brands)>0:
		allProducts=allProducts.filter(brand__id__in=brands).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(productattribute__size__id__in=sizes).distinct()
	t=render_to_string('ajax/product-list.html',{'data':allProducts})
	return JsonResponse({'data':t})

def product_list(request):
    total_data = Product.objects.count()
    data=Product.objects.all().order_by('-id')[:8]
    min_price=ProductAttribute.objects.aggregate(Min('price'))
    max_price=ProductAttribute.objects.aggregate(Max('price'))

    context = {
        'total_data': total_data,
        'data': data,
        'min_price': min_price,
        'max_price': max_price
    }
    return render(request, 'list.html', context)


# Load More
def load_more_data(request):
	offset=int(request.GET['offset'])
	limit=int(request.GET['limit'])
	data=Product.objects.all().order_by('-id')[offset:offset+limit]
	t=render_to_string('ajax/product-list.html',{'data':data})
	return JsonResponse({'data':t}
)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'faq.html')

def delivery_info(request):
    return render(request, 'delivery_info.html')


def conditions(request):
    return render(request, 'conditions.html')


def returns_refunds(request):
    return render(request, 'returns_refunds.html')
