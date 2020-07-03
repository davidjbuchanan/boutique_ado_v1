from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        # get size info. from request. Set equal to none initially and add if appropriate
    bag = request.session.get('bag', {})
    # creating an HTTP session variable
    #   check to see if there's a bag variable in the session. And if not we'll create one as a regular Python object as a dictionary

    if size:
        if item_id in list(bag.keys()):
"""If the item is already in the bag. Then we need to check if another item of the same id and same size already exists. And if so increment the quantity for that size and otherwise just set it equal to the quantity."""

            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity

            else:
                bag[item_id]['items_by_size'][size] = quantity

        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
"""Let's start with the else block. If the items not already in the bag we just need to add it. But we're actually going to do it as a dictionary with a key of items_by_size. Since we may have multiple items with this item id. But different sizes. This allows us to structure the bags such that we can have a single item id for each item. But still track multiple sizes."""

    else:
        if item_id in list(bag.keys()):
        # If the item is already in the bag in other words if there's already a key in the bag dictionary matching this product id.
            bag[item_id] += quantity
            # Then I'll increment its quantity accordingly.
        else:
            bag[item_id] = quantity
            # If the item is not already listed within the bag dictionary, I'll just create a key of the item's id and set it equal to the quantity.

    request.session['bag'] = bag
    # Now I just need to put the bag variable into the session, which itself is just a python dictionary. Here we are overwriting the variable in the session with the updated version.
    print(request.session['bag'])
    return redirect(redirect_url)
    # All that's left now is to import redirect. And then redirect the user back to the redirect URL.