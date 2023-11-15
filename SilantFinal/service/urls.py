from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('maintenances/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('reclamations/', ReclamationListView.as_view(), name='reclamation_list'),
    path('machine/<pk>/maintenances', MaintenanceMachineListView.as_view(), name='machine_maintenance'),
    path('machine/<pk>/reclamations', ReclamationMachineListView.as_view(), name='machine_reclamation'),
    path('maintenance/create', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('reclamation/create', ReclamationCreateView.as_view(), name='reclamation_create'),
    path('maintenance/<pk>/update', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('reclamation/<pk>/update', ReclamationUpdateView.as_view(), name='reclamation_update'),
    path('maintenance/<pk>/delete', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('reclamation/<pk>/delete', ReclamationDeleteView.as_view(), name='reclamation_delete'),
    path('maintenance/<pk>/description/<atribute>', MaintenanceDescriptionView.as_view(),
         name='maintenance_description'),
    path('reclamation/<pk>/description/<atribute>', ReclamationDescriptionView.as_view(), name='reclamation_description'),

    path('api/maintenances/', MaintenanceListAPI.as_view(), name='maintenance_list_api'),
    path('api/<user>/maintenances/', MaintenanceUserListAPI.as_view(), name='user_maintenance_list_api'),
    path('api/maintenance/<pk>/', MaintenanceDetailAPI.as_view(), name='maintenance_detail_api'),
    path('api/reclamations/', ReclamationListAPI.as_view(), name='reclamation_list_api'),
    path('api/<user>/reclamations/', ReclamationUserListAPI.as_view(), name='user_reclamation_list_api'),
    path('api/reclamation/<pk>/', ReclamationDetailAPI.as_view(), name='reclamation_detail_api'),
]
