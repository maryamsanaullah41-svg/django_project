from django.urls import path
from myapp import views

urlpatterns = [
    # 1. Main Home Page Dashboard (Search Filter + A-Z Sorting)
    path('', views.home_view, name='home_view'),
    
    # 2. Dynamic Details Page (User Profiles Details)
    path('details/<int:id>/', views.detail_view, name='details'),
    
    # 3. Frontend Form Page (Insert New Data)
    path('create/', views.create_profile_view, name='create_profile'),
    
    # 4. Delete Profile Page (Remove Data with Confirmation)
    path('delete/<int:id>/', views.delete_profile_view, name='delete_profile'),
    path('edit/<int:id>/', views.edit_profile_view, name='edit_profile'),
]