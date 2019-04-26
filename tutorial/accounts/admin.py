from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import category,category1,category2,category3,category4
from accounts.models import contact
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(category)
admin.site.register(category1)
admin.site.register(category2)
admin.site.register(category3)
admin.site.register(category4)
admin.site.register(contact)
