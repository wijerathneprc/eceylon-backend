from django.urls import path

from .views import RamListView, RamCreateView, StorageCreateView, SimCardCreateView, BatteryCreateView, ColorCreateView, GraphicCardCreateView, ColorListView



urlpatterns = [

 path('ram/list', RamListView.as_view(), name='ram-list'),
 path('ram/', RamCreateView.as_view(), name='ram-create'),
 path('color/list', ColorListView.as_view(), name='color-list'),
 path('color/', ColorCreateView.as_view(), name='color-create'),
 
 
  path('storage/create', StorageCreateView.as_view(), name='storage-create'),
 path('battery/create', BatteryCreateView.as_view(), name='battery-create'),
 
  path('graphics/create', GraphicCardCreateView.as_view(), name='graphic-create'),
 path('ram/create', RamCreateView.as_view(), name='ram-create'),
 
  path('simcard/create', SimCardCreateView.as_view(), name='sim-card-create'),
 
 
#   path('ram/list', RamListView.as_view(), name='ram-list'),
#  path('ram/create', RamCreateView.as_view(), name='ram-create'),
 
 
 ]