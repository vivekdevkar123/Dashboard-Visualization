# urls.py
from django.urls import path
from .views import InsightList, InsightDetail,import_data_view

urlpatterns = [
    path('api/insights/', InsightList.as_view(), name='insight-list'),
    path('api/insights/<int:pk>/', InsightDetail.as_view(), name='insight-detail'),
    path('import-data/', import_data_view, name='import-data'),  # Add this line
]
