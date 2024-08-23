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
    d={}
    m=0
    j=1
    li=[]
    di={}
    if x is None:
            return 0
    else:
        for x, obj in x.items():
            j=0
            #print("\nx ",x,"obj ",obj,"\n")
            for obj, i in obj.items():