from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
         model = Contact
         fields = '__all__' # include name, ph number and city
        
        