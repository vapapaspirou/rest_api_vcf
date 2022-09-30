"""demo URL Configuration

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

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from vcf_demo import views
from vcf_demo.views import ApiListView

urlpatterns = [
    path('products/', views.snippet_list),
    path('products/<int:pk>/', views.snippet_detail),
    path('list/', ApiListView.as_view(), name='list'),

]


urlpatterns = format_suffix_patterns(urlpatterns)