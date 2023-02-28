from django.urls import path
from . import views
app_name='mobileapp'

urlpatterns = [

 path('',views.index,name='index'),
 path('apple/<int:apple_id>/',views.nextpage,name='nextpage'),
 path('add/',views.add_apple,name='add_apple'),
 path('update/<int:id>/',views.update,name='update'),
 path('delete/<int:id>/',views.delete,name='delete')


]