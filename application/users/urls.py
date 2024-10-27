from .views import ContactPostGet, ContactsByID
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('get_all/', ContactPostGet.as_view(), name='contact-post-get'),
    path('<int:contact_id>/', ContactsByID.as_view(), name='contact-by-id'),
]
