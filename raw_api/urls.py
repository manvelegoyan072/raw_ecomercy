from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('raw_api/', include('products.urls')),
    path('raw_api/auth/', include('accounts.urls')),
    path('raw_api/cart/', include('cart.urls')),
    path('raw_api/orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


schema_view = get_schema_view(
    openapi.Info(
        title="REST API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]