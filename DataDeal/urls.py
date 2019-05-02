"""DataDeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from DataDealApp.views import GetTest, GetTestasd
from django.conf.urls import url, include
from DataDeal.views import department_frequency_port, classification_number_port, deparment_class_sort_out, sort_out

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/', GetTest),
    path(r'a/', GetTestasd, name='a'),
    path(r'department_frequency_port/', department_frequency_port),
    path(r'classification_number_port/', classification_number_port),
    path(r'deparment_class_sort_out/', deparment_class_sort_out),
    path(r'sort_out/', sort_out),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
