from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email']

    def validate_email(self, value):
        if Contact.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_phone_number(self, value):
        if not value.startswith("+") or not value[1:].isdigit():
            raise serializers.ValidationError("Phone number must start with '+' and contain only digits.")
        return value

    def validate(self, data):
        if not data.get('username') and data.get('email'):
            data['username'] = data['email'].split('@')[0]
        return data