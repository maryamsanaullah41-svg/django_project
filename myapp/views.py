from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile

# 1. Main Dashboard View (Search Filter + Sorting)
def home_view(request):
    query = request.GET.get('search')
    
    if query:
        profiles = UserProfile.objects.filter(username__icontains=query).order_by('username')
    else:
        profiles = UserProfile.objects.all().order_by('username')
        
    context = {
        'profiles': profiles,
        'query': query
    }
    return render(request, 'index.html', context)

# 2. Dynamic Profile Details View
def detail_view(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    return render(request, 'details.html', {'profile': profile})

# 3. Frontend Form View (Insert New Profile)
def create_profile_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        
        UserProfile.objects.create(username=username, email=email, bio=bio)
        return redirect('home_view')
        
    return render(request, 'create_profile.html')

# 4. Delete Profile View (Remove Data)
def delete_profile_view(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    
    if request.method == 'POST':
        profile.delete()
        return redirect('home_view')
        
    return render(request, 'delete_confirm.html', {'profile': profile})
# 5. Edit Profile View (Update Data)
def edit_profile_view(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    
    if request.method == 'POST':
        profile.username = request.POST.get('username')
        profile.email = request.POST.get('email')
        profile.bio = request.POST.get('bio')
        profile.save() # Updated details database mein save ho jayengi
        return redirect('home_view')
        
    return render(request, 'edit_profile.html', {'profile': profile})