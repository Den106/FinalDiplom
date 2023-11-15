from rest_framework import serializers
from .models import *
from service.serializers import ServiceCompanySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ModelOfMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelOfMachine
        fields = '__all__'

class ModelOfMotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelOfMotor
        fields = '__all__'

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = '__all__'

class TypeOfMainAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfMainAxle
        fields = '__all__'

class TypeOfSteeringAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfSteeringAxle
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):
    machine_model = ModelOfMachineSerializer()
    motor_model = ModelOfMotorSerializer()
    transmission_model = TransmissionSerializer()
    main_axle_model = TypeOfMainAxleSerializer()
    steering_axle_model = TypeOfSteeringAxleSerializer()
    service_company = ServiceCompanySerializer()
    client = UserSerializer()
    class Meta:
        model = Machine
        fields = '__all__'
