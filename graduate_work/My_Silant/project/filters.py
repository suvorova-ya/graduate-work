from django_filters import FilterSet
from .models import Machine,Maintenance_operation,Reclamation
import django_filters


class MachineFilter(FilterSet):
   class Meta:
       model = Machine
       fields = (
           'model_drive_axle',
           'model_guiding_axle',
           'model_transmission',
           'model_engine',
           'model_mashine',
           )
       
class MaintenanceFilter(django_filters.FilterSet):
    
    id_number = django_filters.ModelChoiceFilter(
        field_name='machine',
        queryset=Machine.objects.all(),
        label='Модель техники'
    )
    
   
    machine = django_filters.CharFilter(
        field_name='machine__id_number',
        label='Зав.№ машины'
       
    )

    class Meta:
        model = Maintenance_operation
        fields = ('machine', 'id_number')

       
       
class Maintenance_operationFilter(FilterSet):
   class Meta:
       model = Maintenance_operation
       fields = (
           'services_company',
           'type_maintenance_operation',
           'machine',
           
           )
       
       
class ReclamationFilter(FilterSet):
   class Meta:
       model = Reclamation
       fields = (
           'services_company',
           'repairing_type',
           'failure_description',
           )
       
class ReclamationMFilter(FilterSet):
    id_number = django_filters.ModelChoiceFilter(
        field_name='machine',
        queryset=Machine.objects.all(),
        label='Модель техники'
    )
    
   
    machine = django_filters.CharFilter(
        field_name='machine__id_number',
        label='Зав.№ машины'
       
    )    

    class Meta:
       model = Reclamation
       fields = ('machine', 'id_number')
              

