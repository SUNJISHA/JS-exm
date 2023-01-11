from django.urls import path
from . import views


app_name='js'

urlpatterns=[
    path('list',views.list,name='listing')

]
