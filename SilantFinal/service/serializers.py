from rest_framework import serializers
from .models import *
class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = '__all__'

class TypeOfMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfMaintenance
        fields = '__all__'

class TypeOfRefusalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfRefusal
        fields = '__all__'

class MethodOfRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodOfRepair
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    type = TypeOfMaintenanceSerializer()
    service_company = ServiceCompanySerializer()
    class Meta:
        model = Maintenance
        fields = '__all__'

class ReclamationSerializer(serializers.ModelSerializer):
    type_of_refusal = TypeOfRefusalSerializer()
    method_of_repair = MethodOfRepairSerializer()
    service_company = ServiceCompanySerializer()
    class Meta:
        model = Reclamation
        fields = '__all__'
