from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name="detail"),
    path('finches/create/', views.FinchCreate.as_view(), name="finches_add"),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name="finches_update"),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name="finches_delete"),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name="add_sighting"),
    path('places/', views.PlaceList.as_view(), name="places"),
    path('places/create/', views.PlaceCreate.as_view(), name="places_add"),
    path('finches/<int:finch_id>/assoc_place/<int:place_id>/', views.assoc_place, name="assoc_place"),
    path('finches/<int:finch_id>/remove_place/<int:place_id>/', views.remove_place, name="remove_place"),
    
]
