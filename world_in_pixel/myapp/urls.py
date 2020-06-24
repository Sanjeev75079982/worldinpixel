from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.user_login,name='user_login'),
    path('pricing/',views.pricing,name='pricing'),
    path('checkout/',views.checkout,name='checkout'),
    # path('favourite/<int:id>',views.favourite,name='favourite')
    
]