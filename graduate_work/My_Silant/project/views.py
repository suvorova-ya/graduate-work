from django.shortcuts import render, get_object_or_404
from project.models import *
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .filters import MaintenanceFilter,ReclamationMFilter
from django.conf import settings
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from rest_framework import viewsets,mixins
from .serializers import *

# Главная страница
class Index(ListView):
    model = Machine
    template_name = 'project/index.html'
    context_object_name = 'machine'
    
  
# Поиск на главной странице
class SearchResultsView(ListView):
    model = Machine
    template_name = 'project/search_results.html'
    context_object_name = 'machine'
    
    def get_queryset(self): 
        query = self.request.GET.get('number')
        machine = Machine.objects.filter(id_number__icontains=query) 
        return machine

# Страница после регистрации
class MainPage(LoginRequiredMixin,ListView):
    model = Machine
    template_name = 'project/main_page.html'

# общая инфо
class Machinelist(LoginRequiredMixin,ListView):
    model = Machine
    template_name = 'lists/machine_list.html'
    context_object_name = 'machines'
    paginate_by = 2
    
    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.role == 'CLIENT':
            print(user.role)
            return Machine.objects.filter(client=self.request.user)
        elif user.role == 'SERVICE_COMPANY':
            print(user.role)
            return Machine.objects.filter(services_company=self.request.user)
        else:
            return Machine.objects.all()
    

    # ТО
class Maintenance_operationlist(LoginRequiredMixin,ListView):
    model = Maintenance_operation
    template_name = 'lists/maintenance_operation.html'
    context_object_name = 'maintenance_operations'
    paginate_by = 3
   
    
    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = MaintenanceFilter(self.request.GET, queryset)
       return self.filterset.qs
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context 
   
class Reclamationlist(LoginRequiredMixin,ListView):
    model = Reclamation
    template_name = 'lists/reclamationlist.html'
    context_object_name = 'reclamation'
    paginate_by = 3
   
    
    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = ReclamationMFilter(self.request.GET, queryset)
       return self.filterset.qs
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context 
   
class Model_Mashinelist(LoginRequiredMixin,ListView):
    model = ModelMashine
    template_name = 'lists/model_mashine.html'
    context_object_name = 'model_mashine'
    paginate_by = 3

class Model_Enginelist(LoginRequiredMixin,ListView):
    model = ModelEngine
    template_name = 'lists/model_engine.html'
    context_object_name = 'model_engine'
    paginate_by = 3

class Model_Transmissionlist(LoginRequiredMixin,ListView):
    model = ModelTransmission
    template_name = 'lists/model_transmission.html'
    context_object_name = 'model_transmission'
    paginate_by = 3
    
class Model_DriveAxlelist(LoginRequiredMixin,ListView):
    model = ModelDriveAxle
    template_name = 'lists/model_drive_axle.html'
    context_object_name = 'drive_axle'
    paginate_by = 3

class Type_MO_list(LoginRequiredMixin,ListView):
    model = Type_Maintenance_operation
    template_name = 'lists/type_mo_list.html'
    context_object_name = 'maintenance_operation'
    paginate_by = 3

class Model_GuidingAxlelist(LoginRequiredMixin,ListView):
    model = ModelGuidingAxle
    template_name = 'lists/model_guidin_axle.html'
    context_object_name = 'guidin_axle'
    paginate_by = 3
    
class FailureDescriptionlist(LoginRequiredMixin,ListView):
    model = FailureDescription
    template_name = 'lists/failure_description.html'
    context_object_name = 'failure_description'
    paginate_by = 3
    
class RepairingTypelist(LoginRequiredMixin,ListView):
    model = RepairingType
    template_name = 'lists/repairing_typelist.html'
    context_object_name = 'repairing_type'
    paginate_by = 3
    
    
  # Добавление справочников 
class MachineCreate(PermissionRequiredMixin,CreateView):
    form_class = MachineForm
    model = Machine
    template_name = 'create/machine_create.html'
    permission_required = ('project.add_machine', )
    
class Maintenance_Create(PermissionRequiredMixin,CreateView):
    form_class = Maintenance_operationForm
    model = Maintenance_operation
    template_name = 'create/maintenance_create.html'
    permission_required = ('project.add_maintenance_operation', )


        
class Reclamation_Create(PermissionRequiredMixin,CreateView):
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'create/reclamation_create.html'
    permission_required = ('project.add_reclamation', )

class ModelMashine_Create(PermissionRequiredMixin,CreateView):
    form_class = ModelMashineForm
    model = ModelMashine
    template_name = 'create/modelMashine_create.html'
    permission_required = ('project.add_modelmashine', )
    
class ModelEngine_Create(PermissionRequiredMixin,CreateView):
    form_class = EngineForm
    model = ModelEngine
    template_name = 'create/modelEngine_create.html'
    permission_required = ('project.add_modelengine', )

class ModelTransmission_Create(PermissionRequiredMixin,CreateView):
    form_class = TransmissionForm
    model = ModelTransmission
    template_name = 'create/modelTransmission_create.html'
    permission_required = ('project.add_modeltransmission', )
    
class ModelDriveAxle_Create(PermissionRequiredMixin,CreateView):
    form_class = DriveAxleForm
    model = ModelDriveAxle
    template_name = 'create/modelDriveAxle_create.html'
    permission_required = ('project.add_modeldriveaxle', )
    
class ModelGuidingAxle_Create(PermissionRequiredMixin,CreateView):
    form_class = GuidingAxleForm
    model = ModelGuidingAxle
    template_name = 'create/modelGuidingAxle_create.html'
    permission_required = ('project.add_modelguidingaxle', )

class Type_Maintenance_operation_Create(PermissionRequiredMixin,CreateView):
    form_class = TypeMOForm
    model = Type_Maintenance_operation
    template_name = 'create/typeMO_create.html' 
    permission_required = ('project.add_type_maintenance_operation', ) 


class FailureDescription_Create(PermissionRequiredMixin,CreateView):
    form_class = FailureDescriptionForm
    model = FailureDescription
    template_name = 'create/failureDescription_create.html' 
    permission_required = ('project.add_failuredescription', ) 

class RepairingType_Create(PermissionRequiredMixin,CreateView):
    form_class = RepairingTypeForm
    model = RepairingType
    template_name = 'create/repairingType_create.html'
    permission_required = ('project.add_repairingtype', )  
    
 # Изменение справочников 
class MachineUpdate(PermissionRequiredMixin,UpdateView):
    form_class = MachineForm
    model = Machine
    template_name = 'create/machine_create.html'
    permission_required = ('project.change_machine', )  
    
class Maintenance_Update(PermissionRequiredMixin,UpdateView):
    form_class = Maintenance_operationForm
    model = Maintenance_operation
    template_name = 'create/maintenance_create.html'
    permission_required = ('project.change_maintenance_operation', )  
    
class Reclamation_Update(PermissionRequiredMixin,UpdateView):
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'create/reclamation_create.html'
    permission_required = ('project.change_reclamation', )  

class ModelMashine_Update(PermissionRequiredMixin,UpdateView):
    form_class = ModelMashineForm
    model = ModelMashine
    template_name = 'create/modelMashine_create.html'
    permission_required = ('project.change_modelmashine', )  
    
class ModelEngine_Update(PermissionRequiredMixin,UpdateView):
    form_class = EngineForm
    model = ModelEngine
    template_name = 'create/modelEngine_create.html'
    permission_required = ('project.change_modelengine', )  

class ModelTransmission_Update(PermissionRequiredMixin,UpdateView):
    form_class = TransmissionForm
    model = ModelTransmission
    template_name = 'create/modelTransmission_create.html'
    permission_required = ('project.change_modeltransmission', )  
    
class ModelDriveAxle_Update(PermissionRequiredMixin,UpdateView):
    form_class = DriveAxleForm
    model = ModelDriveAxle
    template_name = 'create/modelDriveAxle_create.html'
    permission_required = ('project.change_modeldriveaxle', )  
    
class ModelGuidingAxle_Update(PermissionRequiredMixin,UpdateView):
    form_class = GuidingAxleForm
    model = ModelGuidingAxle
    template_name = 'create/modelGuidingAxle_create.html'
    permission_required = ('project.change_modelguidingaxle', )  

class Type_Maintenance_operation_Update(PermissionRequiredMixin,UpdateView):
    form_class = TypeMOForm
    model = Type_Maintenance_operation
    template_name = 'create/typeMO_create.html'  
    permission_required = ('project.change_type_maintenance_operation', )  


class FailureDescription_Update(PermissionRequiredMixin,UpdateView):
    form_class = FailureDescriptionForm
    model = FailureDescription
    template_name = 'create/failureDescription_create.html'  
    permission_required = ('project.change_failuredescription', )  

class RepairingType_Update(PermissionRequiredMixin,UpdateView):
    form_class = RepairingTypeForm
    model = RepairingType
    template_name = 'create/repairingType_create.html'
    permission_required = ('project.change_repairingtype', )   

 # Удаление справочников 
class MachineDelete(PermissionRequiredMixin,DeleteView):
    model = Machine
    template_name = 'delete/machine_delete.html'
    success_url = reverse_lazy('machine_list')
    permission_required = ('project.delete_machine', ) 
    
class Maintenance_Delete(PermissionRequiredMixin,DeleteView):
    model = Maintenance_operation
    template_name = 'delete/maintenance_delete.html'
    success_url = reverse_lazy('maintenance_operation')
    permission_required = ('project.delete_maintenance_operation', ) 
    
class Reclamation_Delete(PermissionRequiredMixin,DeleteView):
    model = Reclamation
    template_name = 'delete/reclamation_delete.html'
    success_url = reverse_lazy('reclamation')
    permission_required = ('project.delete_reclamation', ) 
    
class ModelMashine_Delete(PermissionRequiredMixin,DeleteView):
    model = ModelMashine
    template_name = 'delete/modelMashine_delete.html'
    success_url = reverse_lazy('model_mashinelist')
    permission_required = ('project.delete_modelmashine', ) 
    
class ModelEngine_Delete(PermissionRequiredMixin,DeleteView):
    model = ModelEngine
    template_name = 'delete/modelEngine_delete.html'
    success_url = reverse_lazy('model_enginelist')
    permission_required = ('project.delete_modelengine', ) 

class ModelTransmission_Delete(PermissionRequiredMixin,DeleteView):
    model = ModelTransmission
    template_name = 'delete/modelTransmission_delete.html'
    success_url = reverse_lazy('model_transmissionlist')
    permission_required = ('project.delete_modeltransmission', ) 
    
class ModelDriveAxle_Delete(PermissionRequiredMixin,DeleteView):
    model = ModelDriveAxle
    template_name = 'delete/modelDriveAxle_delete.html'
    success_url = reverse_lazy('model_drive_axlelist')
    permission_required = ('project.delete_modeldriveaxle', ) 
    
class ModelGuidingAxle_Delete(PermissionRequiredMixin,DeleteView):
    model = ModelGuidingAxle
    template_name = 'delete/modelGuidingAxle_delete.html'
    success_url = reverse_lazy('model_guidin_axlelist')
    permission_required = ('project.delete_modelguidingaxle', ) 

class Type_Maintenance_operation_Delete(PermissionRequiredMixin,DeleteView):
    model = Type_Maintenance_operation
    template_name = 'delete/typeMO_delete.html'
    success_url = reverse_lazy('type_mo_list')  
    permission_required = ('project.delete_type_maintenance_operation', ) 


class FailureDescription_Delete(PermissionRequiredMixin,DeleteView):
    model = FailureDescription
    template_name = 'delete/failureDescription_delete.html' 
    success_url = reverse_lazy('failure_descriptionlist') 
    permission_required = ('project.delete_failuredescription', ) 

class RepairingType_Delete(PermissionRequiredMixin,DeleteView):
    model = RepairingType
    template_name = 'delete/repairingType_delete.html' 
    success_url = reverse_lazy('repairing_typelist') 
    permission_required = ('project.delete_repairingtype', ) 
    
def permission_denied_view(request, exception):
    return render
    
    
#  API   
class MachineViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Machine.objects.all().order_by('-delivery_date')
    serializer_class = MachineSerializer

    
class Maintenance_operationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Maintenance_operation.objects.all().order_by('-date_maintenance_operation')
    serializer_class = Maintenance_operationSerializer


class ReclamationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Reclamation.objects.all().order_by('-date')
    serializer_class = ReclamationSerializer

