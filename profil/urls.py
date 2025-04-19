from django.urls import path
from .views import *

app_name = 'profil'
urlpatterns = [
    path('', profil_view, name='profil'),
    path('profil_edit/', edit_profile, name='edit_profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('my_tests/', my_tests, name='my_tests'),
    path('delete_test/<int:id>/', delete_test, name='delete_test'),

]
