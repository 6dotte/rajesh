from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages
from users.models import NewUser
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def sitemap(request):
    return render(request,'sitemap.xml')

def robots(request):
    return render(request,'robots.txt')    

def seo_common(request,page):
    seo = SEO.objects.filter(page__icontains=page)    
    seo_dic = {}
    i=0
    for obj in seo:
        seo_temp = {
            "page_title":obj.page_title,
            "page_desc":obj.page_desc,
            "page_keyword":obj.page_keyword,
            "schema":obj.schema
        }
        seo_dic[i] = seo_temp
        i = i+1
    return seo_dic

def login(request):
    page_title = "Login | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

    return redirect('/')


def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            logout(request)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def index(request):
    page_title = "MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    services = Services.objects.all()
    testimonials = Testimonials.objects.all()[:3]
    logos = ClientLogos.objects.all()
    about_obj = About.objects.all()[:1]
    slider_banners = SliderBanner.objects.all()
    attributes = SliderAttributes.objects.all()

    return render(request, 'index.html', {'attributes':attributes,'about':about_obj,'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'services': services, 'testimonials': testimonials, 'logos': logos,'slider_banners':slider_banners})


def about(request):
    page_title = "About Us | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""


    about_obj = About.objects.all()

    return render(request, 'about.html', {'about':about_obj,'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def award(request):
    page_title = "award | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    award = Awards.objects.all()

    return render(request, 'award.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'award': award})


def contact(request):

    page_title = "Contact | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email,
                               subject=subject, message=message)

    return render(request, 'contact.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def faq(request):

    page_title = "FAQs | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    faqs = Faq.objects.all()

    context = {'page_title': page_title,
               'meta_desc': meta_desc,
               'keyword': keyword,
               'schema': schema,
               'faqs': faqs
               }

    return render(request, 'faq.html', context)


def error(request):
    page_title = "MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    return render(request, 'error.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def thankyou(request):
    page_title = "MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    return render(request, 'thankyou.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def privacy(request):
    page_title = "Privacy | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    return render(request, 'privacy.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def terms_condition(request):
    page_title = "Terms | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    return render(request, 'terms_condition.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema})


def service_detail(request, slug):
    page_title = "Services | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    services = Services.objects.values('title', 'slug')
    details = Services.objects.get(slug=slug)

    return render(request, 'service_detail.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'details': details, 'services': services, 'slug': slug})


@login_required(login_url='login')
def dashboard(request):
    page_title = "Dashboard | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    bills = Bills.objects.filter(user_id=request.user.id)

    return render(request, 'dashboard.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'bills': bills})


def blogs(request):
    page_title = "blogs | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    blogs = Blogs.objects.all()

    return render(request, 'blogs.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'blogs': blogs})


def blog_detail(request, pk):
    page_title = "blogs | MK Brothers"
    meta_desc = ""
    keyword = ""
    schema = ""

    blogs = Blogs.objects.filter().exclude(id=pk)
    blogs_detail = Blogs.objects.filter(id=pk)

    return render(request, 'blog_detail.html', {'page_title': page_title, 'meta_desc': meta_desc, 'keyword': keyword, 'schema': schema, 'blogs': blogs, 'blogs_detail': blogs_detail})


def update_profile(request):
    name = request.POST.get('name')
    email = request.POST.get('email_id')
    mobile_no = request.POST.get('mobile_no')
    location = request.POST.get('location')

    user_id = request.user.id

    res = NewUser.objects.filter(pk=user_id).update(
        name=name, mobile_no=mobile_no, email=email, location=location)

    return redirect('/dashboard')


def change_profile_pic(request):

    user_id = request.user.id
    user = NewUser.objects.get(pk=user_id)
    user.profile_pic = request.FILES['profile_pic']
    user.save()

    return redirect('/dashboard')


def add_bills(request):

    user_id = request.user.id
    title = request.POST.get('title')
    file = request.FILES['file']
    message = request.POST.get('message')
    now=datetime.today().strftime('%Y-%m-%d')

    Bills.objects.create(user_id=user_id, title=title,
                         file=file, message=message, date=now)

    return redirect('/dashboard')

def delete_bills(request):
    pk=request.GET['id']
    user_id = request.user.id
    Bills.objects.filter(pk=pk).filter(user_id=user_id).delete()

    return redirect('/dashboard')


def edit_bills(request):

    # user_id = request.user.id
    title = request.POST.get('title')
    files = request.FILES['file']
    message = request.POST.get('message')
    id = request.POST.get('id')
    date = request.POST.get('date')

    Bills.objects.filter(pk=id).update(
        title=title, file=files, message=message, date=date)

    return redirect('/dashboard')
