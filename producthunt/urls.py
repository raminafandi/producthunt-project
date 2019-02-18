from django.contrib import admin
from django.urls import path
from products import views
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home,name='home'),
    path('accounts/',include('accounts.urls')),
]
