from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('<int:id>/delete',views.delete_new, name='widget_delete')
]