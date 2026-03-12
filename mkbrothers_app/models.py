from django.db import models
from django.db.models.fields import related
from users.models import NewUser
from datetime import datetime

# Create your models here.
TRENDING_CHOICES = (
    ("Home Page", "Home Page"),
    ("About Us", "About Us"),
    ("Awards", "Awards"),
    ("Blogs", "Blogs"),
    ("Contact Us", "Contact Us"),
    ("FAQ", "FAQ")
)

class SEO(models.Model):
  page = models.CharField(max_length=550, choices = TRENDING_CHOICES) 
  page_title = models.TextField(blank= True) 
  page_keyword = models.TextField(blank= True) 
  page_desc = models.TextField(blank= True)
  schema = models.TextField(blank= True) 

  def __str__(self):
   return self.page
  class Meta:
        verbose_name_plural = "SEO"  

class About(models.Model):
    about = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    successfull_years = models.CharField(max_length=55, default=" ", null=True)
    employees = models.CharField(max_length=55, default=" ", null=True)
    awards = models.CharField(max_length=55, default=" ", null=True)
    branches = models.CharField(max_length=55, default=" ", null=True)
    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about

class BlogCategory(models.Model):
    name = models.CharField(max_length=210, default=None)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


class Blogs(models.Model):
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, default=None, blank=True)
    image = models.FileField(blank=True, default=None)
    slug = models.CharField(max_length=550, default=" ", null=True)
    blog = models.TextField(blank=True, null=True)
    blog_date = models.DateField(max_length=550, null=True, default=None)
    author = models.CharField(max_length=550, default=" ", null=True)
    tag = models.CharField(max_length=550, default=" ", null=True)
    page_title = models.CharField(max_length=550, default=" ", null=True)
    page_keyword = models.CharField(max_length=550, default=" ", null=True)
    page_desc = models.CharField(max_length=550, default=" ", null=True)
    schema = models.TextField(blank=True)
    is_popular = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class Faq(models.Model):
    category = models.CharField(max_length=550, default=" ")
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Faqs"


class Bills(models.Model):

    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, default=None, blank=True)
    file = models.FileField(null=True, blank=True)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Bills"


class Awards(models.Model):
    title = models.CharField(max_length=200, default=None, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Awards"


class Services(models.Model):
    title = models.CharField(max_length=200, default=None, blank=True)
    image = models.FileField(blank=True, default=None)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"


class Contact(models.Model):

    name = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"


class Testimonials(models.Model):

    name = models.CharField(max_length=200, default=None, blank=True)
    image = models.ImageField(blank=True, default=None)
    designation = models.CharField(max_length=150, default=None, blank=True)
    testimonial = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Testimonials"


class ClientLogos(models.Model):

    title = models.CharField(max_length=200, default=None, blank=True)
    logo = models.ImageField(blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Client Logos"


class SliderAttributes(models.Model):

    attribute = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.attribute

    class Meta:
        verbose_name_plural = "Slider Attributes"

class SliderBanner(models.Model):

    image = models.ImageField(blank=True, default=None, null=True)
    keyword = models.CharField(max_length=200, null=True,blank=True)
    title = models.CharField(max_length=200, default=None, blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Slider Banner"
