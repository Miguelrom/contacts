from django.urls import path

from . import views


urlpatterns = [
    path('', views.ContactListView.as_view(), name='contacts'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),

]

