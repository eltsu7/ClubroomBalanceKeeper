"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns

from balancekeeper.views import stats, ProductView, CbkUserView, CbkUserDetailView, TransactionView, CategoryView, CategoryDetailView, ProductDetailView

urlpatterns = [
    path('cbk/admin/', admin.site.urls),
    path('cbk/stats/', stats),
    path('cbk/product/', ProductView.as_view()),
    path('cbk/product/<uuid:id>/', ProductDetailView.as_view()),
    path('cbk/category/', CategoryView.as_view()),
    path('cbk/category/<uuid:id>/', CategoryDetailView.as_view()),
    path('cbk/user/', CbkUserView.as_view()),
    path('cbk/user/<uuid:id>/', CbkUserDetailView.as_view()),
    path('cbk/user/<uuid:id>/transactions/', TransactionView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
