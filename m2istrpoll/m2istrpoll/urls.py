"""
URL configuration for m2istrpoll project.

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
from election import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.ElectionListView.as_view(), name="elections"),
    path("election/<int:pk>", views.ElectionDetailView.as_view(), name="election"),
    path("candidate/<int:pk>/vote", views.VoteView.as_view(), name="vote"),
]
