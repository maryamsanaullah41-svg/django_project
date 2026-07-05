from django.contrib import admin
from .models import UserProfile

# Admin class banayein jo columns ko display karegi
class UserProfileAdmin(admin.ModelAdmin):
    # Yeh columns admin panel ki main list mein dikhein ge
    list_display = ('id', 'username', 'email')
    
    # Aap admin panel ke andar search bar bhi add kar sakti hain!
    search_fields = ('username', 'email')

# Model ko is nayi custom admin class ke sath register karein
admin.site.register(UserProfile, UserProfileAdmin)