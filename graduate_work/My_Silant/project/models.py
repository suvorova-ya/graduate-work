from django.db import models
from django.conf import settings
from django.utils.text import slugify




class ModelMashine (models.Model):
    #    модель техники
    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Модель техники"
        verbose_name_plural = "Модели техники"

    def __str__(self):
        return f"{self. name}"
    
    def get_absolute_url(self):
       return '/model_mashinelist/'


class ModelEngine (models.Model):
    # Модель двигателя

    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Модель двигателя"
        verbose_name_plural = "Модели двигателя"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return '/model_enginelist/'

class ModelTransmission (models.Model):
    # модель трансмиссии

    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "модель трансмиссии"
        verbose_name_plural = "модели трансмиссии"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return '/model_transmissionlist/'


class ModelDriveAxle (models.Model):
    #    Модель ведущего моста

    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Модель ведущего моста"
        verbose_name_plural = "Модели ведущего моста"

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
       return '/model_drive_axlelist/'

class ModelGuidingAxle (models.Model):
    # Модель управляемого моста

    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Модель управляемого моста"
        verbose_name_plural = "Модели управляемого моста"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return '/model_guidin_axlelist/'

class Machine (models.Model):
    # Машина
    id_number = models.CharField(max_length=128, verbose_name='Зав.№ машины')
    model_mashine = models.ForeignKey(
        ModelMashine, on_delete=models.CASCADE, verbose_name='Модель техники')
    model_engine = models.ForeignKey(
        ModelEngine, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    number_engine = models.CharField(
        max_length=128, verbose_name='Зав.№ двигателя')
    model_transmission = models.ForeignKey(
        ModelTransmission, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    number_transmission = models.CharField(
        max_length=200, verbose_name='Зав.№ трансмиссии')
    model_drive_axle = models.ForeignKey(
        ModelDriveAxle, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    number_drive_axle = models.CharField(
        max_length=200, verbose_name='Зав.№ ведущего моста')
    model_guiding_axle = models.ForeignKey(
        ModelGuidingAxle, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    number_guiding_axle = models.CharField(
        max_length=200, verbose_name='Зав. № управляемого моста')
    delivery_contract = models.CharField(
        max_length=200, verbose_name='Договор поставки №, дата')
    delivery_date = models.DateField(
         verbose_name='Дата отгрузки с завода')
    recipient = models.CharField(
        max_length=200, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(
        max_length=250, verbose_name='Адрес поставки (эксплуатации)')
    equipment_package = models.CharField(
        max_length=500, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, verbose_name='Клиент')
    services_company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Сервисная компания',related_name="auth_user_set")
    # slug = models.SlugField(max_length=250,unique=True, db_index=True, null=True,verbose_name="URL")

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        ordering = ('-delivery_date',)

    def __str__(self):
        return self.model_mashine.name
    
    def get_absolute_url(self):
       return '/machine_list/'
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(rand_slug() + "-" + self.model_mashine)
    #     super(Machine, self).save(*args, **kwargs)
     


class Type_Maintenance_operation(models.Model):
    # Вид ТО
    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Вид ТО"
        verbose_name_plural = "Вид ТО"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return '/type_mo_list/'


class Maintenance_operation(models.Model):
    # техническое обслуживание
    type_maintenance_operation = models.ForeignKey(Type_Maintenance_operation, on_delete=models.CASCADE,
                                                   verbose_name='Вид ТО')
    date_maintenance_operation = models.DateField(
        verbose_name='Дата проведения ТО')
    operation_time = models.IntegerField(null=True,verbose_name='Наработка, м/час')
    number_workshop_order = models.CharField(
        max_length=50, verbose_name='№ заказ-наряда')
    date_workshop_order = models.DateField(verbose_name='дата заказ-наряда')
    services_company = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО')
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, verbose_name='Машина')

    class Meta:
        verbose_name = "Техническое обслуживание"
        verbose_name_plural = "Техническое обслуживание"
        ordering = ('date_maintenance_operation',)

    def __str__(self):
        return str([self.type_maintenance_operation])
    
    def get_absolute_url(self):
       return '/maintenance_operation/'


class FailureDescription(models.Model):
    # характер отказа
    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Характер отказа"
        verbose_name_plural = "Характеры отказа"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return '/failure_descriptionlist/'


class RepairingType(models.Model):
    # способ восстановления
    name = models.CharField(max_length=250,verbose_name='Название')
    description = models.TextField(max_length=600,verbose_name='Описание')

    class Meta:
        verbose_name = "Способ восстановления"
        verbose_name_plural = "Способы восстановления"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return '/repairing_typelist/'

class Reclamation(models.Model):
    # рекламация
    date = models.DateField(verbose_name='Дата отказа')
    operation_time = models.IntegerField(verbose_name='Наработка, м/час')
    failure_description = models.ForeignKey(
        FailureDescription, on_delete=models.CASCADE, verbose_name='Узел отказа')
    description_reclamation = models.TextField(
        max_length=600, verbose_name='Описание отказа')
    repairing_type = models.ForeignKey(
        RepairingType, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    spare_part = models.TextField(
        max_length=250, verbose_name='Используемые запасные части')
    reinstatement_date = models.DateField(verbose_name='Дата восстановления')
    standing_time = models.IntegerField(
        null=True, verbose_name='Время простоя техники')
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE, verbose_name='Машина')
    services_company = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, verbose_name='Организация, проводившая ТО')
    
    def standing_time(self):
        return self.reinstatement_date-self.date

    class Meta:
        verbose_name = "Рекламация"
        verbose_name_plural = "Рекламация"
        ordering = ('date',)

    def __str__(self):
        return str([self.date])
    
    def get_absolute_url(self):
       return '/reclamation/'

