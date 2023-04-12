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
    path('topps/<int:topp_id>/add_offer/', views.add_offer, name='add_offer'),
    path('topps/<int:topp_id>/assoc_company/<int:company_id>/', views.assoc_company, name='assoc_company'),
    path('company/', views.CompanyList.as_view(), name='company_index'),
    path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/update/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company_delete'),
]