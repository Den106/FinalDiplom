from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', MachineSearchView.as_view(), name='machine_search_list'),
    path('machines/', MachineListView.as_view(), name='machine_list'),
    path('machine/<pk>/detail', MachineDetailView.as_view(), name='machine_detail'),
    path('machine/create', MachineCreateView.as_view(), name='machine_create'),
    path('machine/<pk>/update', MachineUpdateView.as_view(), name='machine_update'),
    path('machine/<pk>/delete', MachineDeleteView.as_view(), name='machine_delete'),
    path('machine/<pk>/description/<atribute>', MachineDescriptionView.as_view(), name='machine_description'),

    path('api/machines/',MachineListAPI.as_view(),name='machine_list_api'),
    path('api/<user>/machines/',MachineUserListAPI.as_view(),name='user_machine_list_api'),
    path('api/machine/<pk>/',MachineDetailAPI.as_view(),name='machine_detail_api'),
]
