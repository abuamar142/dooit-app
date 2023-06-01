from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('show_profiles/', views.show_profile_view, name='show_profiles'),
    path('show_profile/', views.show_profile_view, name='show_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_transaction/<int:id>', views.update_transaction, name='update_transaction'),
]