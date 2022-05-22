from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from manager.client import client
from manager.account import account
from django.views.decorators.csrf import csrf_exempt


def signin(request: HttpRequest):
    # if request.method == 'POST':
    #     data = request.POST.dict()
    #     if data['user'] == 'admin' and data['password'] == 'admin':
    #         return render(request, 'index.html')
    # return render(request, 'signin.html')
    return render(request, 'index.html')


def index(request: HttpRequest):
    return render(request, 'index.html')


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
    manager = client()
    if request.method == 'POST':
        client_id = request.POST.dict()['client_id']
        try:
            manager.delete(client_id)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')

    if 'query' in request.GET.dict():
        query = request.GET.dict()['query']
        client_list = []
        try:
            result = manager.search_id(query)
            client_list.append(result)
        except:
            pass
        try:
            results = manager.search_name(query)
            client_list.extend(results)
        except:
            pass
        return render(request, 'client/search.html', {
            'query': query,
            'num': len(client_list),
            'client_list': client_list
        })
    return render(request, 'client/search.html')


def account_search(request: HttpRequest):
    manager = account()
    if request.method == 'POST':
        account_id = request.POST.dict()['account_id']
        try:
            manager.delete(account_id)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')

    if 'query' in request.GET.dict():
        query = request.GET.dict()['query']
        try:
            account_list = manager.search(query)
        except:
            pass
        return render(request, 'account/search.html', {
            'query': query,
            'num': len(account_list),
            'account_list': account_list
        })
    return render(request, 'account/search.html')


def account_insert_checking(request: HttpRequest):
    if request.method == 'POST':
        manager = account()
        data = request.POST.dict()
        try:
            manager.insert('checking', data)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')
    return render(request, 'account/insert_checking.html')


def account_insert_saving(request: HttpRequest):
    if request.method == 'POST':
        manager = account()
        data = request.POST.dict()
        try:
            manager.insert('saving', data)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')
    return render(request, 'account/insert_saving.html')


def account_update(request: HttpRequest):
    manager = account()
    account_id = request.path[9:13]
    type = manager.account_type(account_id)
    if request.method == 'POST':
        data = request.POST.dict()
        if 'client_id' and 'is_delete' in data:
            try:
                manager.delete_client_visit(data['client_id'], account_id)
            except Exception as e:
                return HttpResponse(e)
            return HttpResponse('success')
        elif 'client_id' in data:
            try:
                manager.add_client_visit(data['client_id'], account_id)
            except Exception as e:
                return HttpResponse(e)
            return HttpResponse('success')
        data['account_id'] = account_id
        try:
            manager.update(type, data)
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('success')
    else:
        dict = manager.search(account_id)[0]
        dict['open_date'] = str(dict['open_date'])
        dict['client_visit_list'] = manager.client_visit(account_id)
        return render(request, 'account/update_%s.html' % type, dict)