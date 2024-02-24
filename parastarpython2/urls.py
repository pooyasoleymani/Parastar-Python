"""
URL configuration for parastarpython2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user.views import user_request
from django.urls import path
from todo.views import TodoListView
from servicerequest.views import ServiceRequestView
# from . import views
from servicecatalog.views  import ServiceCatalogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-user/',user_request),
    path('api/create-user/<int:id>',user_request),
    path('todos/', TodoListView.as_view()),
    path('todos/<int:id>/', TodoListView.as_view()),
    path('serviceRequest/', ServiceRequestView.as_view()),
    path('serviceRequest/<int:id>/', ServiceRequestView.as_view()),
    path('servicecatalog/', ServiceCatalogView.as_view()),
    path('servicecatalog/<int:id>/', ServiceCatalogView.as_view()),
]