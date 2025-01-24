"""
URL configuration for leadmanagement_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from leadmanagement_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead/add/', views.LeadCreateView.as_view(),name="lead_add"),
    path('lead/list/',views.LeadListView.as_view(), name="lead_list"),
    path('lead/<int:pk>/update/', views.LeadUpdateView.as_view(), name="lead_update"),
    path('lead/<int:pk>/delete/', views.LeadDeleteView.as_view(), name="lead_delete"),
]
