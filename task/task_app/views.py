from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from task_app.serializer import UserSerializer, BioSerializer, LoginSerializer, InfoSerializer, customError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from .models import bios



class loginUser(APIView):

	def post(sef, request, format='json'):
		serializer = LoginSerializer(data=request.data)
		if(serializer.is_valid()):
			username = serializer.data['username']
			password = serializer.data['password']
			user = authenticate(username=username, password=password)
			if user:
				mydict = {}
				mydict["email"] = User.objects.get(username = username).email
				mydict["phone_no"] = bios.objects.get(username = username).phone_no
				mydict["username"] = username
				return_serializer = InfoSerializer(data=mydict)
				
				if(return_serializer.is_valid()):
				# 	return_serializer.save()

					json = return_serializer.data
					return Response(json)
			else:
				mydict = {"msg": "Username or password invalid"}
				# json = customError(data = mydict).data
				return Response(mydict, status=status.HTTP_400_BAD_REQUEST)








class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        serializer2 = BioSerializer(data=request.data)
        print(request.data["username"])
        if serializer.is_valid():
        	if serializer2.is_valid():
	            user = serializer.save()
	            bio = serializer2.save()
	            if user:
	                token = Token.objects.create(user=user)
	                json = serializer.data
	                json.update(serializer2.data)
	                print(json)
	                json['token'] = token.key

	                return Response(json, status=status.HTTP_201_CREATED)
	        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



