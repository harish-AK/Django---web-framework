from .models import Contact
from rest_framework import generics
from .serializer import ContactSerializer

# create (POST) and List (GET) contacts,
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    # Retrieve (GET), Update (PATCH/PUT) and Delete (DELETE) a contact  
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer