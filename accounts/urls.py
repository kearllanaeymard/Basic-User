from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signUpView.as_view(), name='signup'),
]