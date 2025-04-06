from django.urls import path 
from students import views
urlpatterns = [
    path('api/',views.UserListCreateView.as_view(),name='viewset'),
    path('api/<int:id>/',views.UserRetrieveUpdateDeleteView.as_view(),name='studentDataView')
]