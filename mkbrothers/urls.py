
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mkbrothers_app.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', index, name='home'),
    path('', index, name='index'),
    path('login', login, name='login'),
    path('logout', logoutUser, name="logout"),
    path('change_password', change_password, name='change_password'),

    path('about', about, name='about'),
    path('award', award, name='award'),
    path('contact', contact, name='contact'),
    path('blogs', blogs, name='blogs'),
    path('blog_detail/<str:pk>', blog_detail, name='blog_detail'),
    path('faq', faq, name='faq'),
    path('add-bills', add_bills, name='add_bills'),
    path('edit-bills', edit_bills, name='edit_bills'),
    path('delete-bill', delete_bills, name='delete_bills'),

    path('error', error, name='error'),
    path('thankyou', thankyou, name='thankyou'),
    path('privacy', privacy, name='privacy'),
    path('terms-condition', terms_condition, name='terms_condition'),
    path('service/<slug:slug>', service_detail, name='service_detail'),
    path('dashboard', dashboard, name='dashboard'),
    path('update-profile', update_profile, name='update_profile'),
    path('change_profile_pic', change_profile_pic,
            name='change_profile_pic'),
    path('summernote/', include('django_summernote.urls')),



    path('reset_password',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_done.html"),
         name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.index_title = "MKBrothers"
admin.site.site_title = "MKBrothers"
admin.site.site_header = "MKBrothers Admin"
