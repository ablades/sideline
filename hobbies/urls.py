from django.urls import path
from .views import HobbiesListView, HobbiesDetailView, HobbiesCreateView, HobbiesUpdateView, HobbiesDeleteView, HobbiesExploreView
from . import views

urlpatterns = [
    path('', views.home, name='hobbies-home'),
    path('explore/', HobbiesExploreView.as_view(), name='hobbies-explore'),
    path('my-hobbies/', HobbiesListView.as_view(), name='hobbies-list'),
    
    path('hobbies/<int:pk>/', HobbiesDetailView.as_view(), name='hobbies-detail'),
    
    path('hobbies/new/', HobbiesCreateView.as_view(), name='hobbies-create'),
    path('hobbies/<int:pk>/update/', HobbiesUpdateView.as_view(), name='hobbies-update'),
    path('hobbies/<int:pk>/delete/', HobbiesDeleteView.as_view(), name='hobbies-delete'),
    path('hobbies/about/', views.about, name='hobbies-about'),
    path('hobbies/getsideline/', views.get_sideline, name='get-sideline'),
    path('hobbies/pricing/', views.pricing, name='pricing'),
    path('hobbies/locations/', views.locations, name='locations'),
    path('hobbies/freetrial/', views.free_trial, name='free-trial'),
]