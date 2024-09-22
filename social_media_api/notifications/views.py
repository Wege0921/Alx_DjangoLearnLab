from django.shortcuts import render
from .models import Notification

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(read=False)
    context = {'notifications': notifications}
    return render(request, 'notifications/list.html', context)

# Create your views here.
