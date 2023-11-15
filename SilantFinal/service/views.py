from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from vehicles.models import *
from service.models import *
from service.forms import *
from service.serializers import MaintenanceSerializer, ReclamationSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


class MaintenanceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_maintenance'
    model = Maintenance
    template_name = 'service/maintenance_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Maintenance.objects.filter(service_company=profile.service_company)
            except:
                return Maintenance.objects.filter(machine__client=user)
        else:
            return Maintenance.objects.all()


class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'service/maintenance_create.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'service/maintenance_update.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_maintenance'
    model = Maintenance
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'maintenance'
        return context


class ReclamationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_reclamation'
    model = Reclamation
    template_name = 'service/reclamation_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Reclamation.objects.filter(service_company=profile.service_company)
            except:
                return Reclamation.objects.filter(machine__client=user)
        else:
            return Reclamation.objects.all()


class ReclamationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_reclamation'
    model = Reclamation
    form_class = ReclamationForm
    template_name = 'service/reclamation_create.html'
    success_url = reverse_lazy('reclamation_list')


class ReclamationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_reclamation'
    model = Reclamation
    form_class = ReclamationForm
    template_name = 'service/reclamation_update.html'
    success_url = reverse_lazy('reclamation_list')


class ReclamationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_reclamation'
    model = Reclamation
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('reclamation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'сomplaint'
        return context


class MaintenanceMachineListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_maintenance'
    model = Maintenance
    template_name = 'service/maintenance_machine.html'

    def get_queryset(self):
        machine = Machine.objects.get(pk=self.kwargs["pk"])
        return Maintenance.objects.filter(machine=machine)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["machine"] = Machine.objects.get(pk=self.kwargs["pk"])
        return context


class ReclamationMachineListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'service.view_reclamation'
    model = Reclamation
    template_name = 'service/reclamation_machine.html'

    def get_queryset(self):
        machine = Machine.objects.get(pk=self.kwargs["pk"])
        return Reclamation.objects.filter(machine=machine)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["machine"] = Machine.objects.get(pk=self.kwargs["pk"])
        return context


class MaintenanceDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance = Maintenance.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'type':
            context['atribute'] = maintenance.type
            context['description'] = maintenance.type.description
        elif atribute == 'service_company':
            context['atribute'] = maintenance.service_company
            context['description'] = maintenance.service_company.description
        return context


class ReclamationDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reclamation = Reclamation.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'type_of_refusal':
            context['atribute'] = reclamation.type_of_refusal
            context['description'] = reclamation.type_of_refusal.description
        elif atribute == 'method_of_repair':
            context['atribute'] = reclamation.method_of_repair
            context['description'] = reclamation.method_of_repair.description
        elif atribute == 'service_company':
            context['atribute'] = reclamation.service_company
            context['description'] = reclamation.service_company.description
        return context


# API
class MaintenanceListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Maintenance.objects.filter(machine__client=user)
        elif type(user) == str:
            queryset = Maintenance.objects.filter(machine__client__username=user)
        return queryset


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = MaintenanceSerializer

    def get_object(self):
        obj = Maintenance.objects.get(pk=self.kwargs['pk'])
        return obj


class ReclamationListAPI(generics.ListAPIView):
    serializer_class = ReclamationSerializer
    queryset = Reclamation.objects.all()


class ReclamationUserListAPI(generics.ListAPIView):
    serializer_class = ReclamationSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Reclamation.objects.filter(machine__client=user)
        elif type(user) == str:
            queryset = Reclamation.objects.filter(machine__client__username=user)
        return queryset


class ReclamationDetailAPI(generics.RetrieveAPIView):
    serializer_class = ReclamationSerializer

    def get_object(self):
        obj = Reclamation.objects.get(pk=self.kwargs['pk'])
        return obj
