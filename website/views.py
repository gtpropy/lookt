from .models import LaunchEmail
from django.http import JsonResponse

def register_mail(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_email = LaunchEmail(email=email)
        new_email.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_user_mail(request):
    if request.method == 'GET':
        if request.Get.get('key') != '45678Lordshiva':
            return JsonResponse({'status': 'error', 'message': 'Invalid key'})
        emails = LaunchEmail.objects.all()
        return JsonResponse({'emails': list(emails.values())})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
