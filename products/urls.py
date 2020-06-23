from django.urls import path
from products.views import all_products, product_detail

urlpatterns = [
    path('', all_products, name='products'),
    path('<product_id>', product_detail, name='product_detail'),
    #  contains the product Id. Will return the product detail view. Be named product detail.

]