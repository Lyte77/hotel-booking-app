from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_up/', views.sign_up, name="signup"),
    # path('login/', views.login, name='login')
    
]
