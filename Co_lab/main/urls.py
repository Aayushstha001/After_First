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
]