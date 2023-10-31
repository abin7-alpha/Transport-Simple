from django.urls import path

from authorization.api.login import login_user
from authorization.api.register import register_user

urlpatterns = [
    path('register-user', register_user, name='register_user'),
    path('login-user', login_user, name='login_user'),
]
