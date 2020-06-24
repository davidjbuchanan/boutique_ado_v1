from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    # a view to render all products and to show sorting and search queries


    products = Product.objects.all()
    query = None


    # start with it as none at the top of this view to ensure we don't get an error when loading the products page without a search term.


    """
    Since we named the text input in the form as the letter q (see form in base.html or mobile-top-header.html). We can just check if q is in 
    request.get, if it is I'll set it equal to a variable called query (query = request.GET['q']). If the query is blank it's not going to return any
    results. So if that's the case let's use the Django messages framework to attach an error message to the request. And then redirect back to the
    products url.
    Import messages, redirect, and reverse up top.
    """


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            
            """
            If the query isn't blank then use a special object from django.db.models called Q to generate a search query.
            This deserves a bit of an explanation.
            In Django if you use something like product.objects.filter in order to filter a list of products. Everything will be ended together: In the
            case of our queries that would mean that when a user submits a query. In order for it to match the term would have to appear in both the
            product name and the product description. Instead, we want to return results where the query was matched in either the product name or the
            description.
            In order to accomplish this 'or' (as in this or that) logic, we need to use Q
            This is worth knowing because in real-world database operations.
            Queries can become quite complex and using Q is often the only way to handle them.
            Because of that, I'd strongly recommend that you become familiar with this and the other complex database functionality. By reading through
            the queries portion of the Django documentation.
            """
           
           
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            
            
            """ 
            I'll set a variable equal to a Q object. Where the name contains the query. Or the description contains the query. The pipe here is what
            generates the 'or' statement. And the i in front of contains makes the queries case insensitive. With those queries constructed. 
            """


            products = products.filter(queries)
           
           
            # pass the queries (from line above) to the filter method in order to actually filter the products

    context = {
        'products': products,
        'search_term': query,
        # add the query to the context. And in the template call it search term
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # a view to show individual product details
    product = get_object_or_404(Product, pk=product_id)
    # pk means primary key
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
