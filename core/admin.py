from django.contrib import admin

# Register your models here.
from .models import User, Banglore, Mumbai, Chennai
admin.site.register(User)


admin.site.register(Banglore)

admin.site.register(Mumbai)


admin.site.register(Chennai)