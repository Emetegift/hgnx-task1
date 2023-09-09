from django.urls import path
from . import views

urlpatterns = [
    # path('task1/', views.endpoint_view, name='endpoint_view'),
     path('', views.endpoint_view, name='endpoint_view')
]
