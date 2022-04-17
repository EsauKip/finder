

from django.contrib import admin
from django.urls import include, path
from projects import views
urlpatterns = [
    path('',include('projects.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_user, name='registration'),
]   
