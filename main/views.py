from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from datetime import datetime,timedelta,timezone
import jwt
from django.conf import settings
from functools import wraps


# api/v1/users  -> get list of fake users 
# api/v1/user - > post user

"""



"""

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



def generate_jwt_token(payload):
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')
    return token


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        response = request.body
        user = json.loads(response)
        username = user.get("username")
        password = user.get("password")

        result = login_user(username, password)

        if result["status_code"] == 200:
            payload = {
                "user_id": 1,
                "username": username,
                "exp": datetime.now(timezone.utc) + timedelta(hours=1),
                "iat": datetime.now(timezone.utc)
            }
            token = generate_jwt_token(payload)
            return JsonResponse({'token': token, 'message': result["message"], 'status_code': 200})
        else:
            return JsonResponse(result)

    if request.method == 'GET':
        return JsonResponse({
        "message": "This endpoint only accepts POST requests",
        "status_code": 400
    })

    return JsonResponse({
        "message": "This endpoint only accepts POST requests",
        "status_code": 400
    })



def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None



def verification_decorator_for_jwt(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return JsonResponse({"message": "Missing token", "status_code": 401})

        payload = verify_jwt_token(token)
        if not payload:
            return JsonResponse({"message": "Invalid or expired token", "status_code": 401})

        return view_func(request, *args, **kwargs)

    return wrapper


@verification_decorator_for_jwt
@csrf_exempt
def listUsers(request):
    return JsonResponse({"users": users_array, "status_code": 200})