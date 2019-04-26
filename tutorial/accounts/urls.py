from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home),
    path('login/',auth_views.LoginView.as_view(template_name= 'accounts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name="logout"),
    path('register/',views.register,name='register'),
    path('profile/',views.view_profile,name='view_profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_profile'),
    path('contact/',views.contactus,name='contact'),
    path('action/',views.action,name='action'),
    path('education/',views.education,name='education'),
    path('fiction/',views.fiction,name='fiction'),
    path('history/',views.history,name='history'),
    path('drama/',views.drama,name='drama'),
    path('cart/',views.cart,name='cart'),
    
    
]
