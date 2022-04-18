

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_user, name='registration'),
    path('', include('projects.urls'))
]
