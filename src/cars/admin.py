from django.contrib import admin
from .models import Brand, Make, BodyType, Feature, Transmission, Drivetrain, CarDetail, Contact


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TransmisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DrivetrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CarDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'year', 'price')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'phone', 'message')





admin.site.register(Brand, BrandAdmin)
admin.site.register(Make, MakeAdmin)
admin.site.register(BodyType, BodyTypeAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Transmission, TransmisionAdmin)
admin.site.register(Drivetrain, DrivetrainAdmin)
admin.site.register(CarDetail, CarDetailAdmin)
admin.site.register(Contact, ContactAdmin)
