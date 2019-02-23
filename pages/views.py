from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

def index(request):

    item_list = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : item_list,
    }
    return render(request,'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }

    return render(request,'pages/about.html',context)