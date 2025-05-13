from django.urls import path
from .views import ContactListCreateView, ContactDetailView  # Ensure correct import

urlpatterns = [
    path('', ContactListCreateView.as_view(), name='contact-list-create'),  # List/Create
    path('<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),  # Retrieve/Update/Delete
]
