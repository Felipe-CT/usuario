from django.urls import path
from .views import LoginView, login, logout

app_name = 'acceso'

urlpatterns = [
    path('', LoginView.as_view(), name='acceso' ),
    path('success/', login, name='login' ),
    path('logout/', logout, name='logout' ),
]
