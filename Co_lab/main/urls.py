from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about, name="about"),

    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout"),

    path('register-employee/', views.register_employee, name="register-employee"),

    path('create-company-post/', views.create_company_post, name="create-company-post"),
    path('create-employee-post/', views.create_employee_post, name="create-employee-post"),

    path('delete-company-post/<str:pk>/', views.delete_company_post, name="delete-company-post"),
    path('delete-employee-post/<str:pk>/', views.delete_employee_post, name="delete-employee-post"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('company_profile/<str:pk>/', views.companyProfile, name="company-profile"),
]