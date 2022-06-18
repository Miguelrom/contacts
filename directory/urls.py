from django.urls import path

from . import views


urlpatterns = [
    path('contacts/', views.ContactListView.as_view(),
    name='contacts'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(),
    name='contact-detail'),
    path('contacts/<int:pk>/delete/',views.ContactDeleteView.as_view(),
    name='contact-delete'),
    path('contacts/<int:pk>/update/',views.ContactUpdateView.as_view(),
    name='contact-update'),
    path('contacts/create/',views.ContactCreateView.as_view(),
    name='contact-create'),

]

