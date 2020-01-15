from django.urls import path
from .views import DetailUserView, UpdateProfileAvatar

urlpatterns = [
    path('', DetailUserView.as_view()),
    path('update-avatar/', UpdateProfileAvatar.as_view()),
]
