from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('topps/', views.topps_index, name='index'),
    path('topps/<int:topp_id>/', views.topps_detail, name='detail'),
    path('topps/create/', views.ToppCreate.as_view(), name='topps_create'),
    path('topps/<int:pk>/update/', views.ToppUpdate.as_view(), name='topps_update'),
    path('topps/<int:pk>/delete/', views.ToppDelete.as_view(), name='topps_delete'),
    path('topps/<int:topp_id>/add_offer/', views.add_offer, name='add_offer')
]