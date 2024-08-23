from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import requests as rq
import json
import datetime

def attendence_record(cardno):
    data_table = get_data()
    print("attendance",type(data_table))
    xd=datetime.datetime.now()
    date=xd.strftime("%x")
    time=xd.strftime("%X")
    data = {	
                'date':date,
                'time':time
            }
    api = f'https://smart-attendance-56a8d-default-rtdb.firebaseio.com/attendance/{cardno}.json'

    #response = rq.post(api,json=data).text
    response = rq.post(api,json=data).text
    
def cardno():
    
    api = 'https://smart-attendance-56a8d-default-rtdb.firebaseio.com/Card.json'
    data = rq.get(api).text
    x=json.loads(data)
    return x['Card']

def index_1(request):
    xy = cardno()
    print('card: ',xy)
    d=get_data()   
    if d==0:
        #print(cardNo,d[i].get('cardnumber'))
        return HttpResponseRedirect('details/')
    else:     
        if request.method=="POST":
            for i,j in enumerate(d):
                if request.method=="POST" and d[i].get('cardnumber')==xy:
                    attendance=d[i].get('attendance')
                    print(xy,d[i].get('cardnumber'))
                    attendance=swap(attendance)
                    return HttpResponseRedirect("verify")
                
            if request.method=="POST" and d[i].get('cardnumber')!=xy:
                print(xy,d[i].get('cardnumber'))
                return HttpResponseRedirect('details/')
        	    
    return render (request,'index1.html',{'ca':xy})


def details(request):
    cn=cardno()
    get_data()
    attendance=1
    d = {
			'card':cn
	}
    
    print('card details ',cn)
    return render(request,'index.html',d)

def auth():

	payload = {
	        'email':'rima983131@gmail.com',
	        'password':'0123456789',
	        'returnSecureToken':True
	}

	key = 'AIzaSyAf3i42IhvCA-l6cwCh0LzVdr9iVH9203w'
	api = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key='+key

	response = rq.post(api,json=payload).text

	#print(response)

def insert(fname,lname,phoneNo,email,cardId,stream,year,attendance,date,time):

    data = {	
                'firstName':fname,
                'lastName':lname,
                'pnumber':phoneNo,
                'email':email,
                'cardnumber':cardId,
                'stream':stream,
                'year':year,
                'attendance':attendance,
                'date':date,
                'time':time
            }
    api = 'https://smart-attendance-56a8d-default-rtdb.firebaseio.com//bio.json'

    #response = rq.post(api,json=data).text
    response = rq.post(api,json=data).text

    #print(response)
    #return render(request,'index1.html') 


def get_data():
    url='https://smart-attendance-56a8d-default-rtdb.firebaseio.com//bio.json'
    x = rq.get(url).text
    data=json.loads(x)
    print(type(data))
    #print(len(data))
    #print(type(data),data)
    d={}
    i=0
    if data is None:
        return 0
    else:
        for x, obj in data.items():
            d[i]=obj
            i+=1
        print(d[0].get("email"))
    return d

    
        
def swap(attendance):
    attendance+=1
    return attendance



# def tempinsert(cardNo):

# 	data={
#                 'tempCardNo.':cardNo
#         }
# 	api = 'https://smart-attendance-56a8d-default-rtdb.firebaseio.com//Card.json'

# 	#response = rq.post(api,json=data).text
# 	response = rq.post(api,json=data).text

# 	print("temp",response) 
 
def verify(request):
    get_data()
    attendance=1
    card=cardno()
    fname = request.POST.get("firstName")
    lname = request.POST.get("lastName")
    phoneNo = request.POST.get("pnumber")
    email = request.POST.get('email')
    cardId=request.POST.get("cardnumber")
    stream=request.POST.get("stream")
    year=request.POST.get("year")
    print(fname,lname)
    xd=datetime.datetime.now()
    date=xd.strftime("%x")
    time=xd.strftime("%X")
    
    auth()
    if(fname is not None and lname is not None):
        attendence_record(card)
        insert(fname,lname,phoneNo,email,cardId,stream,year,attendance,date,time)
    get_data()
    if fname==None and lname==None:
        attendence_record(card)
        detail=get_data()
        for i,j in enumerate(detail):
            if detail[i].get('cardnumber')==card:
                fname=detail[i].get('firstName')
                lname=detail[i].get('lastName')
                    
    d = {
			'firstname':fname,
            'lastname':lname,
	}  
    print(fname,lname)      
    return render(request, 'verify.html',d)

def index1(request):    
    xy = cardno()
    print('card: ',xy)
    d=get_data() 
    if request.method=="POST":
        return HttpResponseRedirect ('dupli_index1')
    else:
        pass        
                
def get_data_attendance():
    api = 'https://smart-attendance-56a8d-default-rtdb.firebaseio.com/attendance.json'
    data = rq.get(api).text
    x=json.loads(data)
    
    m=0
    j=1
    li=[]
    di={}
    if x is None:
            return 0
    else:
        for x, obj in x.items():
    
            j=0
            d={}

            for obj, i in obj.items():

                d[j]=i      
                j+=1
            
            di[x]=d
            
            
            
        
                      
        return di        
   
d1=get_data_attendance()
print(d1)
def table(request):
    search=request.POST.get('search')
    attendance_record=get_data_attendance()
    print(attendance_record)
    r={}
    data_table = get_data()
    print(type(data_table))
    for i, obj in enumerate(data_table):
        if search==data_table[i].get("email"):
                
            #    email=data_table[i].get("email")
            fname=data_table[i].get("firstName")
            lname=data_table[i].get("lastName")
            phno=data_table[i].get("pnumber")
            time=data_table[i].get("time")
            date=data_table[i].get("date")
            year=data_table[i].get("year")
            dept=data_table[i].get("stream")
            attendance=data_table[i].get("attendance")
            cardno=data_table[i].get("cardnumber")
    for i in attendance_record:
        if cardno==i:
                       
                       #print(cardno)
            print("i= ",i)
            for k,i in attendance_record[i].items():
                print("k: ",k,"i: ",i)
                r[k]=i  
            print(r)
        else:
            pass
    detail={
                   'fname':fname,
                   'lname':lname,
                   'phno':phno,
                   'time':time,
                   'date':date,
                   'year':year,
                   'dept':dept,
                   'attendance':attendance,
                   'cardno':cardno,
                   'a_rec':r
               }
                  
    print(cardno)                 
    return render(request, "table.html" ,detail)


    
        