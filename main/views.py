from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return JsonResponse({
        'message':'success'
    })

mock_users = [
    {"user_id":"101","name":"Aman Kumar Verma","address":"new baradwari"},
    {"user_id":"102","name":"Ravi Sharma","address":"sakchi"},
    {"user_id":"103","name":"Anjali Singh","address":"Baridhi"}
]

# get users
def users(request):
    return JsonResponse({
        "users":mock_users
    })

import json

# post users
@csrf_exempt
def add_users(request):
    response = request.body
    data = json.loads(response)
    for key,value in data.items():
        print(key,value)
    return JsonResponse({
        "users":mock_users
    })



