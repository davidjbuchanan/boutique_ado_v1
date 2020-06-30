from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    # an empty list for the bag items to live in.
    total = 0
    product_count = 0
    # I'll also eventually need the total and the product count when we start adding things to the bag. So I'll initialize those now to zero.

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # check whether it's less than that threshold.
        
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # it is less we'll calculate delivery as the total multiplied by the standard delivery percentage from settings.py. which in this case is 10%
        # I'm using the decimal function since this is a financial transaction and using float is susceptible to rounding errors.
        
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        # For convenience let's also let the user know how much more they need to spend to get free delivery by creating a variable called free_delivery_delta
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
    # The last step is simple, we just need to add all these items to the context. So they'll be available in templates across the site.
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context