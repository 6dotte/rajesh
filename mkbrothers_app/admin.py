from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import *

class AboutAdmin(SummernoteModelAdmin):
    list_display = ['about']
    list_editable = []
    summernote_fields = ["about","mission","vision"]

admin.site.register(About, AboutAdmin)

class SEOAdmin(admin.ModelAdmin):
    list_display = ["page","page_title"]

admin.site.register(SEO, SEOAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_editable = []


admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "slug", "blog_date", "author", "tag"]
    list_editable = []


admin.site.register(Blogs, BlogsAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Faq._meta.fields]
    list_editable = []


admin.site.register(Faq, FaqAdmin)


class BillsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'file', 'message']
    list_editable = []


admin.site.register(Bills, BillsAdmin)


class AwardsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'description', 'image']
    list_editable = []
    summernote_fields = ["description"]


admin.site.register(Awards, AwardsAdmin)


class ServicesAdmin(SummernoteModelAdmin):
    list_display = ['title', 'image', 'description']
    list_editable = []
    summernote_fields = ["description"]


admin.site.register(Services, ServicesAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Contact._meta.fields]
    list_editable = []


admin.site.register(Contact, ContactAdmin)


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Testimonials._meta.fields]
    list_editable = []


admin.site.register(Testimonials, TestimonialsAdmin)


class ClientLogosAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ClientLogos._meta.fields]
    list_editable = []


admin.site.register(ClientLogos, ClientLogosAdmin)


class SliderBannerAdmin(SummernoteModelAdmin):
    list_display = [f.name for f in SliderBanner._meta.fields]
    list_editable = []
    summernote_fields = ["description"]


admin.site.register(SliderBanner, SliderBannerAdmin)


class SliderAttributesAdmin(SummernoteModelAdmin):
    list_display = [f.name for f in SliderAttributes._meta.fields]
    list_editable = []
    summernote_fields = ["attribute"]


# admin.site.register(SliderAttributes, SliderAttributesAdmin)