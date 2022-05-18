from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q



def categories(request):
    return {
        'categories' : Category.objects.all(),
    }


def all_product(request):
    products = Product.objects.all()
    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    prd = p.get_page(page)

    return render(request, 'blog-sell.html',{'products' : products,
                                            'prd':prd})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    #product.num_visits = product.num_visits + 1
    #product.save()

    def get_id(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip=get_id(request)
    u=Product(userip=ip)
    result=Product.objects.filter(Q(userip__icontains=ip))
    count=Product.objects.all().count()
    product.visits = count

    return render(request, 'product-details-sell.html', {'product' : product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    p = Paginator(Product.objects.filter(category=category), 6)
    page = request.GET.get('page')
    cat = p.get_page(page)
    return render(request, 'category.html', {'category':category, 'products':products, 'cat':cat})


def home(request):
    data = Product.objects.filter(is_newproduct=True).order_by('-created')
    return render(request, 'home.html', {'data': data })


def account(request):
    args = {'user': request.user}
    return render(request , 'account.html', args)


def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['con-email']
        msg = request.POST['msg']


        send_mail(
            fullname,
            msg,
            email,
            ['loukmanous12345@gmail.com'],
        )
        messages.success(request, ("Merci, Email a été envoyé"))
        return render(request, 'contact.html', {})
    else:
        return render(request , 'contact.html', {})


def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-created')
    p = Paginator(Product.objects.filter(title__icontains=q).order_by('-created'), 10)
    page = request.GET.get('page')
    searchP = p.get_page(page)
    return render(request, 'search.html', {'data': data, 'searchP':searchP })


