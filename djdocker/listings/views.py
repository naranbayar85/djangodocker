from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.

def Listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def Listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def Listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def Listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def Listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
    