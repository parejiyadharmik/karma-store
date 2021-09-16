from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user)
admin.site.register(add_product)
admin.site.register(Cart)
admin.site.register(category_dtls)