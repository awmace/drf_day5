from django.urls import path

from api import views

urlpatterns=[
    path('test/',views.TestAPIView.as_view())
]