from django.contrib import admin
from django.urls import path

from .views import UsersView, PingView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ping/', PingView.as_view()),

    # Endpoints for user URL.
    path('users/', UsersView.as_view(), name='users'),
    path('users/<uuid:id>/', UsersView.as_view(), name='users')
]
