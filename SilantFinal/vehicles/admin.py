from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
 
# Устанавливаем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )
 
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Модель машины
class ModelOfMachineResource(resources.ModelResource):
    class Meta:
        model = ModelOfMachine
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ModelOfMachine)
class ModelOfMachineAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ModelOfMachineResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Модель двигателя
class ModelOfMotorResource(resources.ModelResource):
    class Meta:
        model = ModelOfMotor
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ModelOfMotor)
class ModelOfMotorAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ModelOfMotorResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Модель трансмиссии
class TransmissionResource(resources.ModelResource):
    class Meta:
        model = Transmission
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(Transmission)
class TransmissionAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TransmissionResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Модель ведущего моста
class TypeOfMainAxleResource(resources.ModelResource):
    class Meta:
        model = TypeOfMainAxle
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TypeOfMainAxle)
class TypeOfMainAxleAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TypeOfMainAxleResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Модель управляемого моста
class TypeOfSteeringAxleResource(resources.ModelResource):
    class Meta:
        model = TypeOfSteeringAxle
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TypeOfSteeringAxle)
class TypeOfSteeringAxleAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TypeOfSteeringAxleResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Машины
class MachineResource(resources.ModelResource):
    class Meta:
        model = Machine
        report_skipped = True
        fields = (
        'id',
        'machine_number',
        'machine_model',
        'motor_model',
        'motor_number',
        'transmission_model',
        'transmission_number',
        'main_axle_model',
        'main_axle_number',
        'steering_axle_model',
        'steering_axle_number',
        'supply_agreement',
        'shipping_date',
        'recipient',
        'shipping_address',
        'equipment',
        'client',
        'service_company',
        )

@admin.register(Machine)
class MachineAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = MachineResource
    list_display = (
        'id',
        'machine_number',
        'machine_model',
        'motor_model',
        'transmission_model',
        'main_axle_model',
        'steering_axle_model',
        'shipping_date',
        'equipment',
        'client',
        'service_company',
    )
    filter = ('machine_number',)
