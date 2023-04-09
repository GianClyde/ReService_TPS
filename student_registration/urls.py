from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.identify, name='identify'),


    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/',views.registerUser,name='register'),
    path('profile-fillup/',views.profile_fillUp,name='profile-fillup'),
    path('reservation',views.reservation,name='reservation'),
    path('reservation-driver-info/<str:pk>/',views.reservation_driver_info,name='driver-info-reservation'),
    path('reservation-process/<str:pk>/',views.reserve_service,name='reserve-service'),


    path('driver-login/', views.driver_login_page, name='driver-login'),
    path('driver-register/', views.driver_register_page, name='driver-register'),
    path('driver-mainNavbPage/',views.drivermainNavPage,name='DrivernavPage'),
    path('driver-profile-fillup/',views.driver_profile_fillUp,name='driver-profile-fillup'),
    path('driver-profile/<str:pk>/', views.driver_security_settings, name='driver-security'),
     path('driver-security-settings/<str:pk>/', views.driver_profile_page, name='driver-profile'),
    path('driver-edit-profile/<str:pk>/', views.edit_driver_profile, name='driver-edit-profile'),

    path('change_password', views.password_change, name='change-password'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),

    
    path('mainNavbPage/',views.mainNavPage,name='navPage'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('edit-profile/<str:pk>/', views.editProfile, name='edit-profile'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('not-allowed', views.not_allowed, name='not-allowed'),
    

]