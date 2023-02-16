from django.contrib import admin
from .models import *


class MachineAdmin(admin.ModelAdmin):
    list_display = ('id','model_mashine', 'delivery_contract','delivery_date', 'recipient', 'delivery_address', 'client')
    list_filter = ('model_mashine', 'delivery_contract','delivery_date', 'recipient', 'client')
    search_fields = ('model_mashine', 'delivery_contract','delivery_date', 'recipient', 'delivery_address', 'client')
    date_hierarchy = ('delivery_date')
    ordering = ['delivery_date']


class Maintenance_operationAdmin(admin.ModelAdmin):
   
    list_display = ('machine', 'type_maintenance_operation',
                    'date_maintenance_operation', 'number_workshop_order', 'date_workshop_order')
    list_filter = ('machine', 'type_maintenance_operation',
                   'date_maintenance_operation', 'number_workshop_order', 'date_workshop_order')
    search_fields = ('machine', 'type_maintenance_operation',
                     'date_maintenance_operation', 'number_workshop_order', 'date_workshop_order')
    date_hierarchy = ('date_workshop_order')
    ordering = ['date_workshop_order']


class ReclamationAdmin(admin.ModelAdmin):
   
    list_display = ('date', 'operation_time', 'repairing_type',
                    'reinstatement_date', 'machine')
    list_filter = ('date', 'operation_time', 'repairing_type',
                   'reinstatement_date', 'machine')
    search_fields = ('date', 'operation_time', 'repairing_type',
                     'reinstatement_date', 'machine')
    date_hierarchy = ('reinstatement_date')
    ordering = ['reinstatement_date']


admin.site.register(ModelMashine)
admin.site.register(ModelEngine)
admin.site.register(ModelTransmission)
admin.site.register(ModelDriveAxle)
admin.site.register(ModelGuidingAxle)
admin.site.register(Type_Maintenance_operation)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Maintenance_operation, Maintenance_operationAdmin)
admin.site.register(FailureDescription)
admin.site.register(RepairingType)
admin.site.register(Reclamation, ReclamationAdmin)
