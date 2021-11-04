from .views import profile, index

from django.urls import path


app_name = "profiles"

urlpatterns = [
    path("profiles/", index, name="index"),
    path("profiles/<str:username>/", profile, name="profile"),
]
