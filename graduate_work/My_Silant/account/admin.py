from django.contrib import admin
from .models import User
from django.contrib.auth import authenticate

def save_model(self, request, obj, form, change):
    obj.save()
    password = form.cleaned_data.get('password')
    obj.set_password(password)
    obj.save()
    user = authenticate(username=obj.username, password=password)
    if user is not None:
        # User is authenticated, you can proceed with your logic
        pass
    else:
        # Authentication failed, you can handle the error here
        pass


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'role',]
    list_filter = ('name', 'role',)
    save_model = save_model

admin.site.register(User, UserAdmin)
