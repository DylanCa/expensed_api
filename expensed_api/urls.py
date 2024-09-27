"""
URL configuration for expensed_api project.

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
from django.urls import path, include
from rest_framework_nested import routers

from api.viewsets.expense_viewset import ExpenseViewSet, PaymentTypeViewSet, CategoryViewSet, MerchantViewSet
from api.viewsets.household_viewset import HouseholdViewSet
from api.viewsets.user_viewset import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'households', HouseholdViewSet)

households_router = routers.NestedSimpleRouter(router, r'households', lookup='household')
households_router.register(r'expenses', ExpenseViewSet, basename='household-expenses')
households_router.register(r'payment_types', PaymentTypeViewSet, basename='household-payment_types')
households_router.register(r'categories', CategoryViewSet, basename='household-categories')
households_router.register(r'merchants', MerchantViewSet, basename='household-merchants')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include(router.urls)),
    path('', include(households_router.urls)),
]
