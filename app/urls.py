from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('detail/<int:id>/', baza_detail, name='baza_detail'),
    path('add_baza/<int:id>', add_baza, name='add_baza'),
    path('bazalar/', bazalar_view, name='bazalar_view'),
    path('add_test/<int:id>/', add_test, name='add_test'),
    path('kategoriya_qoshish/', add_category, name='add_ctg'),
    path('submit_answer/', submit_answer, name='submit_answer'),
    path('delete_baza/<int:id>/', delete_baza, name='delete_baza'),


]
