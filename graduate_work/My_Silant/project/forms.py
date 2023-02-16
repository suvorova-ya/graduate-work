from django import forms
from django.forms import ModelForm
from .models import *

# Формы для создания справочников
class MachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = [
            'id_number',
            'model_mashine',
            'model_engine', 
            'number_engine', 
            'model_transmission',
            'number_transmission',
            'model_drive_axle',
            'number_drive_axle',
            'model_guiding_axle',
            'number_guiding_axle',
            'delivery_contract',
            'delivery_date',
            'recipient',
            'delivery_address',
            'equipment_package',
            'services_company'
                  
            ]
        
class Maintenance_operationForm(ModelForm):
    date_maintenance_operation = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='Дата проведения ТО')
    date_workshop_order =  forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='дата заказ-наряда')  
     
    class Meta:
        model = Maintenance_operation
        fields = [
            'type_maintenance_operation',
            'date_maintenance_operation',
            'operation_time',           
            'number_workshop_order',
            'date_workshop_order',  
            'services_company',
             'machine',
             
            
            
           
                    
            ]
        
class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation
        fields = [
            'date',
            'operation_time',
            'failure_description',
            'description_reclamation',  
            'repairing_type',
            'spare_part',
            'reinstatement_date',
            'machine',
            'services_company'   
            ]
        
class ModelMashineForm(ModelForm):
    class Meta:
        model = ModelMashine
        fields = [
            'name',
            'description'        
            ]

class EngineForm(ModelForm):
    class Meta:
        model = ModelEngine
        fields = [
            'name',
            'description'        
            ]

class TransmissionForm(ModelForm):
    class Meta:
        model = ModelTransmission
        fields = [
            'name',
            'description'        
            ]

class DriveAxleForm(ModelForm):
    class Meta:
        model = ModelDriveAxle
        fields = [
            'name',
            'description'        
            ]
        
class GuidingAxleForm(ModelForm):
    class Meta:
        model = ModelGuidingAxle
        fields = [
            'name',
            'description'        
            ]
        
class TypeMOForm(ModelForm):
    class Meta:
        model = Type_Maintenance_operation
        fields = [
            'name',
            'description'        
            ]   
        
class FailureDescriptionForm(ModelForm):
    class Meta:
        model = FailureDescription
        fields = [
            'name',
            'description'        
            ] 

class RepairingTypeForm(ModelForm):
    class Meta:
        model = RepairingType
        fields = [
            'name',
            'description'        
            ] 
        
