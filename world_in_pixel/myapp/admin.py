from django.contrib import admin
from myapp.models import Category,Image,Subscription,Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Subscription)
admin.site.register(Contact)
