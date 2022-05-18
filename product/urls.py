from django.urls import path
from . import views

app_name= 'product'


urlpatterns = [
    path('all_product/', views.all_product, name="all_product"),
    path('item/<slug:slug>/', views.product_detail, name="product_detail"),
    path('search/<slug:category_slug>/', views.category_list, name="category_list"),
    path('home/', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
    path('account/', views.account, name="account"),
     
]