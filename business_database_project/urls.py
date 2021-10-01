"""business_database_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from online_database import views
from django.conf import settings
from django.conf.urls.static import static
#from ajax_select import ajax_select_urls

urlpatterns = [
    #path('ajax_select/', include(ajax_select_urls)),
    path('admin/', admin.site.urls),
    path('online_database/',include('online_database.urls')),
    path('', RedirectView.as_view(url='/online_database/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


