from django.urls import path
from .views import List_test

urlpatterns=[
    path("list_test",List_test,name='list_test')
]