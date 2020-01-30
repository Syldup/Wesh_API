from django.urls import include, path
from rest_framework import routers, schemas
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.DefaultRouter()
router.register(r'codepromo', views.CodePromoViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token),
    path('auth/', include('rest_framework.urls'), name='api_token_auth'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
    path('openapi/', schemas.get_schema_view(
        title="Wesh API",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]
