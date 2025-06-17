from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from busapp.models import bus,customers,booking_history





# ! validation


def password_validation(password,c_p):
    u_count=0
    l_count=0
    n_count=0
    s_count=0
    if password==c_p:
        if len(password)>=8 :
            for i in password:
                if i.isupper():
                    u_count+=1
                elif i.islower():
                    l_count+=1
                elif i.isdigit():
                    n_count+=1
                else:
                    s_count+=1
            if u_count>0 and l_count>0 and n_count>0 and s_count>0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# !  
def clean_up_history():
    today=date.today() 
    booking=booking_history.objects.filter(travelling_date__lt=today) 
    for i in booking: 
        delete_booking=i.service_no
        # delete_booking=bus.objects.filter(service_no=i.service_no.service_no)
        delete_booking.seats_available += i.no_of_seats
        delete_booking.save()
    booking.delete()
    
    
    
    

def login(request):
    # !
    clean_up_history()
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
# def create(request):
#     return redirect('/')
def create(request):
    name=request.POST.get('name')
    phno=request.POST.get('phno')
    password=request.POST.get('password')
    c_p=request.POST.get('c_p')
    if password_validation(password,c_p) and len(phno)==10:
        data=customers(
            cname=name,
            phno=phno,
            password=password,
        )
        data.save()
        
        return redirect('/')
        # return render(request,'login.html')
    else:
        return render(request,'signup.html',{'error':'username or password is wrong'})

def verify(request):
    name=request.POST.get('u_name')
    password=request.POST.get('pass')
    a=customers.objects.all()
    for i in a:
        if i.cname==name:
            row=customers.objects.filter(cname=name)
            for i in row:
                if i.password==password:
                    request.session['n']=name
                    details=bus.objects.all()
                    return render(request,'home.html',{'res':details})
                else:
                    return render(request,'login.html')
        else:
            return render(request,'login.html')


from datetime import date
import random


def bookbus(request):
    service_no=request.GET.get('service_no')
    price=request.GET.get('price')
    today=str(date.today())
    
    return render(request,'booking.html',{'service_no':service_no,'price':price,'today':today})
    # return render(request,'booking.html')
def cancelbus(request):
    return render(request,'cancel.html')



def conform(request):
    seats=request.GET.get('no_of_seats')
    service_no=request.GET.get('service_no')
    price=request.GET.get('price')
    travelling_date=request.GET.get('travelling_date')
    amount=int(seats)*int(price)
    customer_name=request.session['n']
    a=bus.objects.filter(service_no=service_no)
    # row = a[0]
    # start=row.start
    # end=row.end
    start=a[0].start.upper
    end=a[0].end.upper
    customer_id=customers.objects.filter(cname=customer_name)[0].cid
    customer_instance=customers.objects.get(cid=customer_id)
    bus_instance=bus.objects.get(service_no=service_no)
    tno=f'qwsedr{random.randint(1000,9999)}'
    a=booking_history.objects.create(ticket_no=tno,customer_id=customer_instance,service_no=bus_instance,no_of_seats=seats,amount=amount,travelling_date=travelling_date)
    b=bus.objects.filter(service_no=service_no)[0]
    if b.seats_available >= int(seats):
        b.seats_available -= int(seats)
        b.save()
        return render(request,'ticket.html',{'seats':seats,'service_no':service_no,'amount':amount,'c_n':customer_name,'from':start,'to':end,'t_no':tno,'date':travelling_date})
    else:
        return render(request,'booking.html',{'error':f'AVAILABLE SEATS ARE {b.seats_available} PLEASE CHOOSE OTHER SERVICE'})






# ! background video+



def bucati(request):
    return render(request,'bucati.html')
def l(request):
    return render(request,'l.html')