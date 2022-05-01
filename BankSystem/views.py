from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseGone, HttpResponseNotModified
from django.shortcuts import render
from django.urls import reverse
from manager.client import client
from django.views.decorators.csrf import csrf_exempt


def client_insert(request: HttpRequest):
    if request.method == 'POST':
        manager = client()
        data = request.POST.dict()
        try:
            manager.insert(data)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')
    else:
        return render(request, 'client/insert.html')
