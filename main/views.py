from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

# api/v1/users  -> get list of fake users 
# api/v1/user - > post user

users_array =[
    {
        "user_id" : 1000,
        "username": "user123",
        "password": "securePass!2025"
    }
]

#excrypt data
# generate random id 

def generateRandomId():
    random_number = random.randint(1001, 2000)
    return random_number

@csrf_exempt
def createAccount(request):
    if request.method == 'POST':
       response  = request.body
       user = json.loads(response)

       user["user_id"] = generateRandomId()
       users_array.append(user)

       return JsonResponse({
           "user":user,
           "message":"your account has been created",
           "status_code":200
       })
    
    if request.method == 'GET':
       return JsonResponse({
           "message":"This endpoints only accept POST request",
           "status_code":400
       })
    
    return JsonResponse({
           "message":"error",
           "status_code":400
       })

# check user exits in users_array or not
def login_user(username, password):
    for user in users_array:
        if user["username"] == username and user["password"] == password:
            return {
                "message": "User exists. Login successful",
                "status_code": 200
            }
    return {
        "message": "User does not exist or incorrect credentials",
        "status_code": 400
    }




@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
       response  = request.body
       user = json.loads(response)
       username = user["username"]
       password = user["password"]
       user = login_user(username,password)
       return JsonResponse(user)

    return JsonResponse({
           "message":"This endpoints only accept POST request",
           "status_code":400
       })


@csrf_exempt
def listUsers(request):
    return JsonResponse({
        "users":users_array   
    })
