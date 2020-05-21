from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('contact', views.contact, name="contact"),
    path('appeals', views.appeals, name="appeals"),
    path('sponsor', views.sponsor, name="sponsor"),
    path('events', views.events, name="events"),
    path('blog', views.blog, name="blog"),
    path('blogdetail/<int:pk>/', views.blog_detail, name="blog_detail"),
    path('gallery', views.gallery, name="gallery"),
    path('donation', views.donation, name="donation"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.loginPage, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logoutUser, name="logout"),


]