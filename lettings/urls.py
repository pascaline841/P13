from .views import letting, index

from django.urls import path


app_name = "lettings"

urlpatterns = [
    path("lettings/", index, name="index"),
    path("lettings/<int:letting_id>/", letting, name="letting"),
]
