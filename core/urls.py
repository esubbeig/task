from django.urls import path
from . import views

urlpatterns = [

	path('', views.AddDataView.as_view(), name='add_data'),

	path('ajax/load-subcategory/', views.LoadSubcategory.as_view(), name='ajax_load_subcategory'),
]