from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse


def ReceiveSms(request):
    message_body = request.POST.get('Body', '')  

    resp = MessagingResponse()

    return HttpResponse(str(resp), content_type='text/xml')



