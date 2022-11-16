
from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login_view, name='login_view'),
    path('',views.register, name='register'),
    path('adminpage', views.admin, name='adminpage'),
    path('banglore', views.banglore, name='banglore'),
    path('mumbai', views.mumbai, name='mumbai'),
    path('branchs', views.branchs, name='branchs'),
    path('chennai', views.chennai, name='chennai'),
    path('adminbanglore', views.adminbanglore, name='adminbanglore'),
    path('adminchennai', views.adminchennai, name='adminchennai'),
    path('adminmumbai', views.adminmumbai, name='adminmumbai'),
    path('chart_banglore', views.chart_banglore, name='chart_banglore'),
    path('chart_chennai', views.chart_chennai, name='chart_chennai'),
    path('chart_mumbai', views.chart_mumbai, name='chart_mumbai'),
    path('logout',views.logout, name='logout'),
]