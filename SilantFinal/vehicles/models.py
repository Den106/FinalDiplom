from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_service = models.BooleanField(default=False, blank=True, verbose_name='Является сотрудником сервисной компании')
    service_company = models.ForeignKey(to='service.ServiceCompany',blank=True, null=True, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.user.username} {self.is_service}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ModelOfMachine(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

class ModelOfMotor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'

class Transmission(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'

class TypeOfMainAxle(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'

class TypeOfSteeringAxle(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'

class Machine(models.Model):
    machine_number = models.CharField(unique=True, max_length=12, verbose_name='Зав. № машины')
    machine_model = models.ForeignKey(ModelOfMachine, on_delete=models.CASCADE, verbose_name='Модель техники')
    motor_model = models.ForeignKey(ModelOfMotor, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    motor_number = models.CharField(max_length=12, verbose_name='Зав. № двигателя')
    transmission_model = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(max_length=12, verbose_name='Зав. № трансмиссии')
    main_axle_model = models.ForeignKey(TypeOfMainAxle, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    main_axle_number = models.CharField(max_length=12, verbose_name='Зав. № ведущего моста')
    steering_axle_model = models.ForeignKey(TypeOfSteeringAxle, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    steering_axle_number = models.CharField(max_length=12, verbose_name='Зав. № управляемого моста')
    supply_agreement = models.CharField(max_length=20, verbose_name='Договор поставки №, дата')
    shipping_date = models.DateField(default=datetime.now, verbose_name='Дата отгрузки с завода')
    recipient = models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')
    shipping_address = models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=False,verbose_name='Комплектация (доп. опции)', default="Стандарт")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey(to='service.ServiceCompany', on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.machine_number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
