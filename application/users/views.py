from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer

class ContactPostGet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(ContactSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactsByID(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def delete(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)