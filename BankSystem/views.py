from django.contrib import messages
from django.http import HttpRequest, HttpResponse
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


def client_update(request: HttpRequest):
    manager = client()
    client_id = request.path[8:12]
    if request.method == 'POST':
        data = request.POST.dict()
        data['client_id'] = client_id
        try:
            manager.update(data)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')
    else:
        dict = manager.search_id(client_id)
        return render(request, 'client/update.html', dict)


def client_search(request: HttpRequest):
    if 'quiry' in request.GET.dict():
        quiry = request.GET.dict()['quiry']
        manager = client()
        client_list = []
        try:
            result = manager.search_id(quiry)
            client_list.append(result)
        except:
            pass
        try:
            results = manager.search_name(quiry)
            client_list.extend(results)
        except:
            pass
        return render(request, 'client/search.html', {
            'quiry': quiry,
            'num': len(client_list),
            'client_list': client_list
        })
    return render(request, 'client/search.html')