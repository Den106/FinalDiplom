from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources

# Вид технического обслуживания
class TypeOfMaintenanceResource(resources.ModelResource):
    class Meta:
        model = TypeOfMaintenance
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TypeOfMaintenance)
class TypeOfMaintenanceAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TypeOfMaintenanceResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Характер отказа
class TypeOfRefusalResource(resources.ModelResource):
    class Meta:
        model = TypeOfRefusal
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TypeOfRefusal)
class TypeOfRefusalAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TypeOfRefusalResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Способ восстановления
class MethodOfRepairResource(resources.ModelResource):
    class Meta:
        model = MethodOfRepair
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(MethodOfRepair)
class MethodOfRepairAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = MethodOfRepairResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Сервисная компания
class ServiceCompanyResource(resources.ModelResource):
    class Meta:
        model = ServiceCompany
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ServiceCompany)
class ServiceCompanyAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ServiceCompanyResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Техническое обслуживание
class MaintenanceResource(resources.ModelResource):
    class Meta:
        model = Maintenance
        report_skipped = True
        fields = ('id','type','date','time_of_operation','purchase_order_number','purchase_order_date','service_company','machine')

@admin.register(Maintenance)
class MaintenanceAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = MaintenanceResource
    list_display = ('id','type','date','time_of_operation','purchase_order_number','purchase_order_date','service_company','machine')
    filter = ('date',)

# Рекламация
class ReclamationsResource(resources.ModelResource):
    class Meta:
        model = Reclamation
        report_skipped = True
        fields = ('id','date_of_refusal','time_of_operation','type_of_refusal','specification_of_refusal','method_of_repair','repair_parts','date_of_repair','downtime','machine','service_company')

@admin.register(Reclamation)
class ReclamationsAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ReclamationsResource
    list_display = ('id','date_of_refusal','time_of_operation','type_of_refusal','date_of_repair','downtime','machine','service_company')
    filter = ('date_of_refusal',)
