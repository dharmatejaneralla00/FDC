from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='/'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('track-awb/', views.TrackAWB),
    path('add-activity/', views.AddActivity, name='add-activity/'),
    path('add-shipment/', views.AddShipment, name='add-shipment/'),
    path('track/',views.track,name='track/')
]
