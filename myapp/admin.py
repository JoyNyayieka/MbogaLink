from django.contrib import admin
from myapp.models import User, Contact, Subscriber, Member, VendorMember, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Member)
admin.site.register(VendorMember)
admin.site.register(Product)
