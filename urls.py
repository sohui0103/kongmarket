from django.contrib import admin
from django.urls import path, include
from market.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls')),
    path('account/', include('account.urls')),
]
