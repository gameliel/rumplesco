import json

from django.http import JsonResponse

from .models import Whatsapp

def api_add_whatsapp(request):
    data = json.loads(request.body)
    phone_number = data['phone_number']

    s = Whatsapp.objects.create(phone_number=phone_number)

    return JsonResponse({'success': True})