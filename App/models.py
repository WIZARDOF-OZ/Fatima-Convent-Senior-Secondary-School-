from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.html import format_html

# Create your models here.
class About(models.Model):
    title = models.CharField(null=True, max_length=100)
    principal_heading = models.CharField(max_length=100)
    principal_content = models.TextField()
    principal_image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    our_story_heading = models.CharField(max_length=100)
    our_story_content = models.TextField()
    about_school_heading = models.CharField(max_length=100)
    about_school_content = models.TextField()
    

    def __str__(self):
        return self.title



# Model for customizing banner page
class Banner(models.Model):
    # MAX_IMAGES = 3
    title = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='banner_images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        )
    add_date =models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html(f'<img src="/media/{self.image}" style="width: 100px;" />')
    # preview_image = models.ImageField(upload_to='banner_images/previews/', editable=True)
    
    def __str__(self) -> str:
        return self.title


# Dashboard Model
class Dashboard(models.Model):
    banner_title = models.CharField(max_length=100)
    total_students = models.IntegerField(default=0)
    total_teachers = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)
    upcoming_events = models.TextField(blank=True)
    notifications = models.TextField(blank=True)
    add_date =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.banner_title} Dashboard"
    
# Gallery Model 
def validate_file_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.mp4']
    extension = str(value.name).lower().split('.')[-1]
    if extension not in valid_extensions:
        raise models.ValidationError("Unsupported file extension. Only JPG, PNG, and MP4 files are allowed.")
    
class GalleryItem(models.Model):
    category = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to='gallery/photos/', 
        null=True, 
        blank=True,
        )
    video = models.FileField(
        upload_to='gallery/videos/', 
        null=True, 
        blank=True,
        )

    def __str__(self):
        return f"{self.category} - {self.subtitle}"

