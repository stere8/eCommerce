from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contactForm
from django.conf import settings
# Create your views here.


def contact(requset):
    title = 'Contact'
    form = contactForm(requset.POST or None)
    context = {'title' : title, 'form' : form}
    confirm_message = None
    if form.is_valid():
        print(form.cleaned_data['email'])
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject ='Message from my site'
        emailFrom = form.cleaned_data['email']
        message ='%s \n by %s \n reply to %s' %(comment , name, emailFrom)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo)
        title = "Thanks !"
        confirm_message = "Thank %s we will get back to you" %(name)
        form = None
        context = {'title': title, 'confirm': confirm_message}
    template = 'contact.html'
    return render(requset,template,context)