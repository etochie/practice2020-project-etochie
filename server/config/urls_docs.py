from rest_framework import permissions
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='SibDevPractice API',
        default_version='v1',
        description="""This is a project for the [Sib Dev 2020 Practice](https://sibdev.pro/practice/)
        
The `swagger-ui` view can be found [here](/swagger).
The `ReDoc` view can be found [here](/redoc).
The swagger YAML document can be found [here](swagger.yaml).""",
        contact=openapi.Contact(email="etochie@mail.ru")
    ),
    public=True,
    permission_classes = (permissions.AllowAny, )
)

urlpatterns = [
    url(r'swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
