"""
URL configuration for goodreads project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from .views import home_page , landing_page
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Books List Api",
        default_version='v1',
        description="Goodreads  New Project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email='xurramovotabek568@gmail.com'),
        license=openapi.License(name="demo license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny ,]
)



urlpatterns = ([
    path('admin/', admin.site.urls),
    path('' ,landing_page , name="landing_page"),
    path('home/' , home_page , name="home_page"),
    path('users/' , include('users.urls') , name="users"),
    path('books/' , include('books.urls') , name="books"),
    path('api/v1/' , include('api.urls') , name="api"),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/' , include('dj_rest_auth.urls')),
        path('api/v1/dj-rest-auth/registration/' , include('dj_rest_auth.registration.urls')),
        # swagger
        path('swagger/' , schema_view.with_ui(
            'swagger' , cache_timeout=0) , name='schema-swagger-ui'),
        path('redoc/' , schema_view.with_ui(
            'redoc' , cache_timeout=0) , name='schema-redoc-ui'),
])+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
