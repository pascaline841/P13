from django.contrib import admin
from django.urls import include, path

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('profiles/', include(('profiles.urls', 'profiles'))),
    path('lettings/', include(('lettings.urls', 'lettings'))),
    path('admin/', admin.site.urls),
]