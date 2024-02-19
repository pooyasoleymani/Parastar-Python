from django.urls import path
from todolist.views import TodoListView
from . import serviceRequestViews
from . import views


from todolist.myviews  import serviceCatalogViews

urlpatterns = [
  path('todos/', views.TodoListView.as_view()),
  path('todos/<int:id>/', views.TodoListView.as_view()),
  path('serviceRequest/', serviceRequestViews.ServiceRequestView.as_view()),
  path('serviceRequest/<int:id>/', serviceRequestViews.ServiceRequestView.as_view()),
  path('servicecatalog/', serviceCatalogViews.ServiceCatalogView.as_view()),
  path('servicecatalog/<int:id>/', serviceCatalogViews.ServiceCatalogView.as_view()),
]