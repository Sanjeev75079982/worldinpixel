from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.user_login,name='user_login'),
    path('pricing/',views.pricing,name='pricing'),
    path('checkout/<int:pk>/',views.checkout,name='checkout'),
    path('about_us/',views.aboutus,name='aboutus'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('terms_of_use/',views.terms_of_use,name='terms_of_use'),
    path('licennse_agreement', views.agreement, name='agreement'),
    path('contact_us/',views.contactus,name='contactus'),
]