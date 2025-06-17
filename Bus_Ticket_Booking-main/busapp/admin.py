from django.contrib import admin

# Register your models here.
from busapp.models import *

# admin.site.register(bus)


@admin.register(bus)
class bus(admin.ModelAdmin):
    list_display=('service_no','start','end','seats_available','price',)
    # add one bus element in buss used in admin
    search_fields=['service_no','price']
    
    
    
@admin.register(customers)
class customers(admin.ModelAdmin):
    list_display=('cid','cname','phno','password',)
    
    
    

@admin.register(booking_history)
class booking_history(admin.ModelAdmin):
    list_display=('ticket_no','customer_id','service_no','no_of_seats','amount','travelling_date')
    search_fields=['ticket_no']
    
    