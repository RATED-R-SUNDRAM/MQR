from django.contrib import admin
from .models import Contact,Medical,Resume,QR

admin.site.register((Contact))
admin.site.register((Medical))
admin.site.register((Resume))
admin.site.register((QR))



# Register your models here.
