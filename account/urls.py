from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('sign_up/', views.sign_up, name="signup"),
    # path('login/', views.login, name='login')
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view() ,name='password_change_done')
    
]
