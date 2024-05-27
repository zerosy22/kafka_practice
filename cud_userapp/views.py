from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Signup
from .serializers import SignupSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@csrf_exempt
@api_view(['POST'])
def signupAPI(request):
    data = request.data
    # print(data)

    required_fields = [
        'SETBX_ID', 'USER_EMAIL', 'USER_PWD', 'USER_NAME', 'USER_PHONE',
        'user_sex', 'USER_BIRTH', 'USER_ADULT', 'USER_ADULT_KEY',
        'USER_LIKE_GENRE', 'USER_LIKE_VOD'
    ]
    
    # Check if all required fields are in the data
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return Response({"error": f"Missing fields: {', '.join(missing_fields)}"}, status=400)
    
    # If all fields are present, process the data
    try:
        data['SETBX_ID'] = int(data['SETBX_ID'])
    except (ValueError, TypeError):
        return Response({"error": "Invalid SETBX_ID"}, status=400)
    
    # Save data using serializer
    serializer = SignupSerializer(data=data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)