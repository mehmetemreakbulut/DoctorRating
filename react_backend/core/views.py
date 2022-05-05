from .serializers import DoctorSerializer, PatientSerializer
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Doctor, Patient
from rest_framework.response import Response
import json
from rest_framework import serializers, viewsets,status
# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    queryset = Patient.objects.all()
    data = {}
        
        
    username = request.data['username']
    print(username)
    password = request.data['password']

    try:

        P = Patient.objects.get(username=username)
    except BaseException as e:
            
        return Response({'message':'Geçersiz kullanıcı adı'},status=status.HTTP_401_UNAUTHORIZED)
        

    if not (password==P.password):
            
        return Response({'message': 'Mail Adresi veya Şifre Hatalı'},status=status.HTTP_401_UNAUTHORIZED)
    else:
        Res = {"username":username}
                
        return Response(Res,status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def DoctorUpdate(request):
    DoctorObject = Doctor.objects.get(id=request.data['id'])
    doctorSerializer = DoctorSerializer(DoctorObject,data=request.data, partial=True)
    if doctorSerializer.is_valid():
    
        newPoint = int(request.data['point'])
        #data = json.dumps(doctorSerializer.data) 
        rating = doctorSerializer.data['rating']
        numberOfVoters = doctorSerializer.data['numberOfVoters']
        newRating = ((rating * numberOfVoters)+newPoint)/(numberOfVoters+1)
        
        object = doctorSerializer.update(DoctorObject,newRating)
        object.save()
        
        
        
        print(object.rating)
        return Response({'rating':object.rating,'numberOfVoters':object.numberOfVoters},status=status.HTTP_200_OK)