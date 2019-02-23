from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

def listings(request):
    item_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(item_list,6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings' : page_listings,
    }
    return render(request,'listing/listing.html', context)

def listing_view(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)

    context ={
        'listing':listing,

    }
    return render(request,'listing/listing_view.html',context)

def search(request):
    return render(request,'listing/search.html')