from django.urls import path
from . import views


urlpatterns = [
    path('',views.ListCreateMember.as_view(),name='member_list'),
    path('<int:pk>/',views.RetrieveUpdateDestroyMember.as_view(), name='member_details'),
    path('<int:member_pk>/activities/',views.ListCreateActivity.as_view(),name='activity_list'),
    path('<int:member_pk>/activities/<int:pk>/',views.RetrieveUpdateDestroyActivity.as_view(),name='activity_details'),

]