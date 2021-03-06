"""bookstore_project URL Configuration

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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_playground.views import GraphQLPlaygroundView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # Django Admin
    path(f'{os.environ.get("ADMIN_URL", default="books-admin")}/', admin.site.urls),
    #  User management
    path('accounts/', include('allauth.urls')),
    # Local apps
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
    path('api/', include('apis.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),
]
# + static(settings.STATIC_URL, document_root=settings.AWS_STATIC_LOCATION + '/')

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
