from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from vehicles.models import Machine, UserProfile

class TypeOfMaintenance(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вид технического обслуживания'
        verbose_name_plural = 'Виды технических обслуживаний'

class TypeOfRefusal(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характеры отказа'

class MethodOfRepair(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'

class ServiceCompany(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'

class Maintenance(models.Model):
    type = models.ForeignKey(TypeOfMaintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    date = models.DateField(default=datetime.now, verbose_name='Дата проведения ТО')
    time_of_operation = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    purchase_order_number = models.CharField(max_length=20, verbose_name='№ заказ-наряда')
    purchase_order_date = models.DateField(default=datetime.now, verbose_name='Дата заказ-наряда')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО', null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')

    def __str__(self):
        return f'{self.date} {self.machine}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'

class Reclamation(models.Model):
    date_of_refusal = models.DateField(default=datetime.now, verbose_name='Дата отказа')
    time_of_operation = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    type_of_refusal = models.ForeignKey(TypeOfRefusal, on_delete=models.CASCADE, verbose_name='Узел отказа')
    specification_of_refusal = models.TextField(blank=True, null=True, verbose_name='Описание отказа')
    method_of_repair = models.ForeignKey(MethodOfRepair, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    repair_parts = models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')
    date_of_repair = models.DateField(default=datetime.now, verbose_name='Дата восстановления')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания', null=True, blank=True)

    def __str__(self):
        return f'{self.date_of_refusal} {self.machine}'

    def downtime(self):
        deltatime = self.date_of_repair - self.date_of_refusal
        return deltatime.days

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
