import requests
from django.http import JsonResponse

class IPRegionRestrictionMiddleware:
    ALLOWED_COUNTRIES = ["UA", "PL"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        country_code = self.get_country_code_from_ip(ip)

        if country_code not in self.ALLOWED_COUNTRIES:
            return JsonResponse({'error': 'Access is restricted to certain regions.'}, status=403)

        response = self.get_response(request)
        return response

    def get_country_code_from_ip(self, ip):
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return data.get('country')
