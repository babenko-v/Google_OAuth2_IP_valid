from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email']

    def validate_email(self, value):
        contact_id = self.instance.id if self.instance else None

        if Contact.objects.exclude(id=contact_id).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use by another contact.")

        return value

    def validate_phone_number(self, value):
        if not value.startswith("+") or not value[1:].isdigit() or len(value) != 13:
            raise serializers.ValidationError("Phone number must start with '+', and be 13 characters long including the '+'")
        return value

    def validate(self, data):
        if not data.get('username') and data.get('email'):
            data['username'] = data['email'].split('@')[0]
        return data