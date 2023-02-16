from django.urls import path,include
from. import views
from rest_framework import routers
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  
from drf_yasg import openapi  
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="My Silant",
      default_version='v1',
      description="API My Silant",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register('machines', views.MachineViewSet, basename='machines')
router.register('maintenance_operations', views.Maintenance_operationViewSet, basename='maintenance_operations')
router.register('reclamations', views.ReclamationViewSet, basename='reclamations')



urlpatterns = [
path('', views.Index.as_view(), name='index'),#главная страница
path('search/', views.SearchResultsView.as_view(), name='search_results'),
path('main_page/',views.MainPage.as_view(), name='main_page'),
# list
path('machine_list/', views.Machinelist.as_view(), name='machine_list'),
path('maintenance_operation/',views.Maintenance_operationlist.as_view(), name='maintenance_operation'),
path('reclamation/',views.Reclamationlist.as_view(), name='reclamation'),
path('model_mashinelist/',views.Model_Mashinelist.as_view(), name='model_mashinelist'),
path('model_enginelist/',views.Model_Enginelist.as_view(), name='model_enginelist'),
path('model_transmissionlist/',views.Model_Transmissionlist.as_view(), name='model_transmissionlist'),
path('model_drive_axlelist/',views.Model_DriveAxlelist.as_view(), name='model_drive_axlelist'),
path('model_guidin_axlelist/',views.Model_GuidingAxlelist.as_view(), name='model_guidin_axlelist'),
path('type_mo_list/',views.Type_MO_list.as_view(), name='type_mo_list'),
path('failure_descriptionlist/',views.FailureDescriptionlist.as_view(), name='failure_descriptionlist'),
path('repairing_typelist/',views.RepairingTypelist.as_view(), name='repairing_typelist'),

# create
path('machine_create/', views.MachineCreate.as_view(), name='machine_create'),
path('maintenance_create/', views.Maintenance_Create.as_view(), name='maintenance_create'),
path('reclamation_create/', views.Reclamation_Create.as_view(), name='reclamation_create'),
path('modelMashine_create/', views.ModelMashine_Create.as_view(), name='modelMashine_create'),
path('modelEngine_create/', views.ModelEngine_Create.as_view(), name='modelEngine_create'),
path('modelTransmission_create/', views.ModelTransmission_Create.as_view(), name='modelTransmission_create'),
path('modelDriveAxle_create/', views.ModelDriveAxle_Create.as_view(), name='modelDriveAxle_create'),
path('modelGuidingAxle_create/', views.ModelGuidingAxle_Create.as_view(), name='modelGuidingAxle_create'),
path('type_Maintenance_operation_create/', views.Type_Maintenance_operation_Create.as_view(), name='type_Maintenance_operation_create'),
path('failureDescription_create/', views.FailureDescription_Create.as_view(), name='failureDescription_create'),
path('repairingType_create/', views.RepairingType_Create.as_view(), name='repairingType_create'),
# update
path('<int:pk>/machine_update/', views.MachineUpdate.as_view(), name='machine_update'),
path('<int:pk>/maintenance_update/', views.Maintenance_Update.as_view(), name='maintenance_update'),
path('<int:pk>/reclamation_update/', views.Reclamation_Update.as_view(), name='reclamation_update'),
path('<int:pk>/modelMashine_update/', views.ModelMashine_Update.as_view(), name='modelMashine_update'),
path('<int:pk>/modelEngine_update/', views.ModelEngine_Update.as_view(), name='modelEngine_update'),
path('<int:pk>/modelTransmission_update/', views.ModelTransmission_Update.as_view(), name='modelTransmission_update'),
path('<int:pk>/modelDriveAxle_update/', views.ModelDriveAxle_Update.as_view(), name='modelDriveAxle_update'),
path('<int:pk>/modelGuidingAxle_update/', views.ModelGuidingAxle_Update.as_view(), name='modelGuidingAxle_update'),
path('<int:pk>/type_Maintenance_operation_update/', views.Type_Maintenance_operation_Update.as_view(), name='type_Maintenance_operation_update'),
path('<int:pk>/failureDescription_update/', views.FailureDescription_Update.as_view(), name='failureDescription_update'),
path('<int:pk>/repairingType_update/', views.RepairingType_Update.as_view(), name='repairingType_update'),
# delete
path('<int:pk>/machine_delete/', views.MachineDelete.as_view(), name='machine_delete'),
path('<int:pk>/maintenance_delete/', views.Maintenance_Delete.as_view(), name='maintenance_delete'),
path('<int:pk>/reclamation_delete/', views.Reclamation_Delete.as_view(), name='reclamation_delete'),
path('<int:pk>/modelMashine_delete/', views.ModelMashine_Delete.as_view(), name='modelMashine_delete'),
path('<int:pk>/modelEngine_delete/', views.ModelEngine_Delete.as_view(), name='modelEngine_delete'),
path('<int:pk>/modelTransmission_delete/', views.ModelTransmission_Delete.as_view(), name='modelTransmission_delete'),
path('<int:pk>/modelDriveAxle_delete/', views.ModelDriveAxle_Delete.as_view(), name='modelDriveAxle_delete'),
path('<int:pk>/modelGuidingAxle_delete/', views.ModelGuidingAxle_Delete.as_view(), name='modelGuidingAxle_delete'),
path('<int:pk>/type_Maintenance_operation_delete/', views.Type_Maintenance_operation_Delete.as_view(), name='type_Maintenance_operation_delete'),
path('<int:pk>/failureDescription_delete/', views.FailureDescription_Delete.as_view(), name='failureDescription_delete'),
path('<int:pk>/repairingType_delete/', views.RepairingType_Delete.as_view(), name='repairingType_delete'),

path('', include(router.urls)),
path('swagger-ui/', TemplateView.as_view(template_name='swaggerui/swaggerui.html',
                                         extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

handler403 = 'project.views.permission_denied_view'
