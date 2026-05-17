from django.shortcuts import render
from django.conf import settings
from App.models import Banner, About, GalleryItem

# Create your views here.

def home(request):
    banner_images = list(Banner.objects.all())
    # print(banner_images)
    return render(request, 'index.html', {'banner_images': banner_images})

def about_view(request):
    about = list(About.objects.all())  
    # print(about)
    data = {
        'about': about,
    }
    return render(request, 'about.html', data)

def error_404(request):
    pass

def contact(request):
    pass

def gallery(request):
    # Get distinct categories from the Gallery model
    distinct_categories = GalleryItem.objects.values_list('category', flat=True).distinct()

    # Fetch all gallery images
    gallery_images = list(GalleryItem.objects.all())


    data = {
        'distinct_categories': distinct_categories,
        'gallery': gallery_images
    }
    print(gallery_images)
    return render(request, 'gallery.html', data)
    
