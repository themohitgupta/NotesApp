from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/upload', views.upload_note, name='upload_note'),
    path('notes/<int:pk>/', views.delete_note, name='delete_note'),
    path('search/', views.search, name='search'),
    path('BCA/FirstYear', views.firstyear, name='firstyear'),
    path('BCA/SecondYear/', views.secondyear, name='secondyear'),
    path('BCA/ThirdYear/', views.thirdyear, name='thirdyear'),
   
]
