from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    # creating an HTTP session variable
    #   check to see if there's a bag variable in the session. And if not we'll create one as a regular Python object as a dictionary

    # Now we can stuff the user's products into it along with the quantity.
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