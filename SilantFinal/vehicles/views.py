from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from vehicles.models import *
from service.models import *
from vehicles.forms import *
from vehicles.serializers import MachineSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


# Главная
class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('machine_list')
        else:
            return redirect('machine_search_list')


class MachineSearchView(ListView):
    model = Machine
    template_name = 'vehicles/machine_search.html'
    queryset = Machine.objects.all()


class MachineListView(LoginRequiredMixin, ListView):
    model = Machine
    template_name = 'vehicles/machine_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Machine.objects.filter(service_company=profile.service_company)
            except:
                return Machine.objects.filter(client=user)
        else:
            return Machine.objects.all()


class MachineDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'vehicles.view_machine'
    model = Machine
    template_name = 'vehicles/machine_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MachineCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_machine'
    model = Machine
    form_class = MachineForm
    template_name = 'vehicles/machine_create.html'
    success_url = reverse_lazy('machine_list')


class MachineUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_machine'
    model = Machine
    form_class = MachineForm
    template_name = 'vehicles/machine_update.html'
    success_url = reverse_lazy('machine_list')


class MachineDescriptionView(TemplateView):
    template_name = 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        machine = Machine.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'machine_model':
            context['atribute'] = machine.machine_model
            context['description'] = machine.machine_model.description
        elif atribute == 'motor_model':
            context['atribute'] = machine.motor_model
            context['description'] = machine.motor_model.description
        elif atribute == 'transmission_model':
            context['atribute'] = machine.transmission_model
            context['description'] = machine.transmission_model.description
        elif atribute == 'main_axle_model':
            context['atribute'] = machine.main_axle_model
            context['description'] = machine.main_axle_model.description
        elif atribute == 'steering_axle_model':
            context['atribute'] = machine.steering_axle_model
            context['description'] = machine.steering_axle_model.description
        elif atribute == 'equipment':
            context['atribute'] = 'Комплектация'
            context['description'] = machine.equipment
        elif atribute == 'service_company':
            context['atribute'] = machine.service_company
            context['description'] = machine.service_company.description
        return context


class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_machine'
    model = Machine
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('machine_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'machine'
        return context


# API
class MachineListAPI(generics.ListAPIView):
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()


class MachineUserListAPI(generics.ListAPIView):
    serializer_class = MachineSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Machine.objects.filter(client=user)
        elif type(user) == str:
            queryset = Machine.objects.filter(client__username=user)
        return queryset


class MachineDetailAPI(generics.RetrieveAPIView):
    serializer_class = MachineSerializer

    def get_object(self):
        obj = Machine.objects.get(pk=self.kwargs['pk'])
        return obj
