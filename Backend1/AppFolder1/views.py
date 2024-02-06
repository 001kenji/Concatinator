from django.shortcuts import render,HttpResponse,loader
from .serilizer import UserSterializer
# Create your views here.
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User

@api_view(['GET'])
def ViewDB(request):
    userDB = User.objects.all().values()
    DBserializer = UserSterializer(userDB, many=True)
    return Response(DBserializer.data)