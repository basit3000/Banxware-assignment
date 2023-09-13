from django.contrib import admin
from django.urls import path
from rest_framework import routers
from historical_balances.hbalances import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Historical balances API",
        default_version="1.0.0",
        description="API documentation of the app."
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('historical-balances/', views.HistoricalBalancesList.as_view(), name='historical-balances-list'),
    path('balances/', views.Balances, name='Balances'),
    path('transactions/', views.Transactions, name='Transactions'),
    path('swagger/schema/', schema_view.with_ui('swagger',cache_timeout=0), name="swagger-schema"),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json')
]
