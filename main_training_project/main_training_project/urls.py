"""main_training_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
# from recommend_app_test.router import router
from recommend_app.router import main_router
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas.coreapi import AutoSchema

# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('recommend_app.urls')),
    # path('',include('recommend_app_test.urls')),
    # path('schema/',schema_view),
    # url(r'^$', schema_view),
    path('',include(main_router.urls))
]
