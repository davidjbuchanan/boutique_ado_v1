from django.urls import path
from bag.views import view_bag

urlpatterns = [
    path('', view_bag, name='view_bag'),

]
