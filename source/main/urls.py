"""main URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('', include('hostelguests.urls')),
                  path('', include('aboutguests.urls')),
                  path('', include('welcomeguests.urls')),
                  path('', include('unwelcomeguests.urls')),
                  path('', include('serviceexecutors.urls')),
                  path('', include('documents.urls')),
                  path('', include('hostelservices.urls')),
                  path('', include('journalservices.urls')),
                  path('', include('products.urls')),
                  path('', include('sellinghistories.urls')),
                  path('', include('productincomes.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('', include('api.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.APP_ENV == "dev":
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
