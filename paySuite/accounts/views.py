from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Username and password are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)
    login(user)
    if user is not None:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def logout_api(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})

# Create your views here.
