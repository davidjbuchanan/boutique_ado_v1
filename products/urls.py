from django.urls import path
from products.views import all_products

urlpatterns = [
    path('', all_products, name='products'),

]