from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='index'),
    path('starter/', views.starter,name='starter'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('service/', views.service,name='service'),
    path('login/', views.login_view, name='login'),
    path('', views.register, name='register'),
]
