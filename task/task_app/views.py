from django.shortcuts import render
# from task_app.json_data import data as cred
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from task_app.serializer import UserSerializer, BioSerializer, LoginSerializer, InfoSerializer, customError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from .models import bios
import matplotlib.pyplot as plt 
import io
import urllib, base64
import gspread
import pandas as pd
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

import matplotlib
import numpy
from matplotlib.dates import date2num
# import matplotlib.pyplot as plt
import json
with open('task_app/json_data.json', 'r') as f:
    my_json_obj = str(json.load(f))


def number(data):
    if data == "" or data == "-":
        return False
  
    return data.isdigit()

def toNum(data):
    n = len(data)
    out = 0
    for i in range (n):
        
        out += int(data[i])
    return out




def complex(st):

	
	    
	top = -1;
	vt = []
	ans = 0;
	i = 0
	while i < (len(st)):
	    
	    if i+1 < len(st) and ((st[i] == 'l'  and st[i+1] == 'o') or (st[i] == 'L' and st[i] == 'o') or (st[i] == 'L' and st[i] == 'O') ):
	        if not(top == -1 or vt[top] == "*" or vt[top] == "+" or st[i] == '+' or st[i] == '*'):
	            vt.append("*");
	            top+=1;
	        
	        vt.append("logn");
	        if ans == 0:
	            ans = 10;
	        
	        else:
	            if vt[top] == "*":
	                ans *=10;
	            else:
	                ans += 10;
	        # print("cut")
	        i+=3;
	        print(i)
	        top+=1;
	    
	    elif st[i] == 'O' or st[i] == 'o' or st[i] == '(' or st[i] == ')' or st[i] == '^' or st[i] == '<' or st[i] == '>' :
	        i+=1;
	        continue;
	    
	    else:
	        if not(top == -1 or vt[top] == "*" or vt[top] == "+" or st[i] == '+'or st[i] == '*'):
	            vt.append("*");
	            top+=1;
	        
	        
	        
	        if not(ans == 0):
	            curr = 0;
	            if (st[i] >= 'a' and st[i] <= 'z') or (st[i] >= 'A' and st[i] <= 'Z'):
	                curr = 100;
	            
	            elif st[i] >= '0' and st[i] <= '9':
	                curr = int(st[i]);
	            
	            if vt[top] == "*" and curr > 0:
	                if(curr < 10):
	                    ans = pow(ans, curr);
	                else:
	                    ans *= curr;
	                
	            
	            elif curr > 0:
	                if curr < 10:
	                    ans += 1;
	                else:
	                    ans += curr
	                    
	            
	            
	        
	        else:
	            if (st[i] >= 'a' and st[i] <= 'z') or (st[i] >= 'A' and st[i] <= 'Z'):
	                ans = 100;
	                
	            else:
	                ans = 1;
	                
	            
	        ths = st[i];
	            
	            
	        vt.append(ths);
	        top+=1;
	    i+=1;
	        
	       
	    
	    
	# for i in range (len(vt)):
	#     print(vt[i]);
	    
	return ans;







def homy(request):
	slug = request.GET.get('slug')
	slug = slug.strip()
	slug2 = request.GET.get('slug2')
	slug2 = slug2.strip()
	team = request.GET.get('team').strip()
	print(slug)
	print(slug2)
	scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

	creds = ServiceAccountCredentials.from_json_keyfile_name("task_app/json_data.json")
	com = 0;


	# In[5]:


	client = gspread.authorize(creds)
	name = "Hard Problems"


	sheet = client.open(team)

	page = sheet.worksheet(slug)

	# print(sheet[2])


	# In[37]:



	# data = sheet.get_all_records()
	data = page.get_all_values()
	# headers = data.pop()
	# print(headers)
	# df = pd.DataFrame(data, columns=headers)

	# print(len(data))

	name_index = {}
	for i in range(len(data[0])):
		if data[0][i] != "":
			# print(data[0][i])
			name_index[data[0][i]] = i;
		# print(name_index);

	if slug2 not in name_index:
		return render(request,'not_found.html',{})
	who = slug2
	com1 = 0
	com_n = 0
	com_n2 = 0
	com_high = 0
	com_lg = 0
	be = 0;
	be_count = 0;
	ae = 0;
	ae_count = 0;
	yes = 0
	progress = [];



	lil = {}
	count = 0;
	times = []
	for i in range(5,len(data[0])):
		if number(data[i][name_index[who]+2]):
			be_count+=1;
			be += toNum(data[i][name_index[who]+2])
		if number(data[i][name_index[who]+3]):
			ae_count+=1;
			ae += toNum(data[i][name_index[who]+3])
		#     if data[i][name_index[who]] == "":
		#         break
		#     else:
		#         print(data[i][5],data[i][6])
		date = data[i][name_index[who]].split(" ")
		#         print(date)
		d  = date[0].split("/")
		if not(data[i][name_index[who]+4] == "" or data[i][name_index[who]+4] =="-"):
			co = complex(data[i][name_index[who]+4])
			if co >= 1000000:
				com_high += 1				
			elif co >= 10000:
				com_n2 += 1
			elif co >= 100:
				com_n += 1
			elif co >= 10:
				com_lg += 1
			else:
				com1 += 1;
				

        
		if len(d) < 2:
			continue;
		
		count+=1;
		
		# print(d)
		ths = int(d[0])+int(d[1])*31+int(d[2])*365;
		if data[i][name_index[who]+1] != "":
			if data[i][name_index[who]+1] != "no" and data[i][name_index[who]+1] != "No" and data[i][name_index[who]+1] != "NO":
				yes += 1;


			# print(data[i][name_index[who]+1])
			if ths in lil.keys():
				lil[ths]+=1
			else:
				lil[ths] = 1
	#         else:
	#             lil.append(0);
	# type(times[0])  
	plt.style.use("seaborn")
	# dts = matplotlib.dates.datestr2num(times)
	# print(dts)
	# dts = matplotlib.dates.date2num(dts)
	# scale_factor = 10
	plt.xlabel("days")
	plt.ylabel("Questions")

	xmin, xmax = plt.xlim()
	ymin, ymax = plt.ylim()

	# plt.xlim(xmin * scale_factor, xmax * scale_factor)
	lists = sorted(lil.items()) # sorted by key, return a list of tuples
	print(lil)
	x, y = zip(*lists)
	y = list(y);
	temp = 0
	for i in range (len(y)):
		temp += y[i]
		progress.append(temp)

	x =numpy.asarray(x)
	x =x - x[0]

	y = numpy.asarray(y)

	# dts = matplotlib.dates.datestr2num(x)
	print(x,y)
	print(count)
	
	
	plt.figure(figsize=(25,10))
	plt.title('daily attemps',fontsize=20)
	plt.plot(x,y)
	plt.xlabel('Days', fontsize=18)
	plt.ylabel('Attemps', fontsize=18)
	fig = plt.gcf()
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	url = urllib.parse.quote(string)
	plt.close()
	plt.title('Progress')
	plt.plot(progress)
	fig = plt.gcf()
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	prg_url = urllib.parse.quote(string)
	plt.close()
	labels = 'high', 'n2', 'n', 'logn','O(1)'
	sizes = []
	sizes.append(com_high)
	sizes.append(com_n2)
	sizes.append(com_n)
	sizes.append(com_lg)
	sizes.append(com1)
	
	colors = 'red','tab:orange','tab:green','tab:blue','brown'

	# sizes = [15, 30, 45, 10]
	explode = (0, 0.1, 0, 0.1,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	# plt.show()
	plt.title('code complexity')
	fig = plt.gcf()
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	url2 = urllib.parse.quote(string)
	com = (com/count)*100
	ae_av = 0;
	if(ae_count > 0):
		ae_av =round(ae/ae_count,2)
	be_av = 0;
	if(be_count > 0):
		be_av = round(be/be_count, 2)
	plt.close()
	return render(request,'home.html',{'data':url,'com1':com1,'com_lg':com_lg,'com_n':com_n,'com_n2':com_n2,
		'com_high':com_high,'slug2':slug2,'count':count,'ae':ae,'ae_count':ae_count,'ae_av':ae_av,
		'be':be, 'be_count':be_count, 'be_av':be_av,'url2':url2,'slug':slug,'yes':yes,'prg_url':prg_url})

def index(request):
	return render(request,'index.html',{})

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



