from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):
   """
         myinfo = Info.objects.first()
            if request.method == 'POST':
                message = request.POST['message']
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
        Context ={'myinfo':myinfo}
        return HttpResponse("this function not work now you can contact me at azmour2016maroc@gmail.com  .")
   """
   Context = {}

   return render(request, 'contact/contact.html', Context)