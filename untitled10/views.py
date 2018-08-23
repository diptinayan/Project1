from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.shortcuts import redirect
import pyrebase

config = {
    'apiKey': "AIzaSyBoro4y2TeqNfmEVlibMvfqUpLGCVODVjc",
    'authDomain': "chalbo-342dd.firebaseapp.com",
    'databaseURL': "https://chalbo-342dd.firebaseio.com",
    'projectId': "chalbo-342dd",
    'storageBucket': "chalbo-342dd.appspot.com",
    'messagingSenderId': "271122013221"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

@csrf_exempt
def post_reservation(request):
    if request.method == 'POST':
        import time
        from datetime import datetime, timezone
        import pytz
        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))
        print("mili" + str(millis))
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        src_loc = request.POST.get('src_loc')
        des_loc = request.POST.get('des_loc')
        email_address = request.POST.get('email_address')
        pass_number = request.POST.get('pass_number')
        car_number = request.POST.get('car_number')
        day_number = request.POST.get('day_number')
        hr_number = request.POST.get('hr_number')
        car_type = request.POST.get('car_type')
        pickup_place = request.POST.get('pickup_place')
        pickup_hrs = request.POST.get('pickup_hrs')

        # idtoken= request.session['uid']
        # a = authe.get_account_info(idtoken)
        # a = a['users']
        # a = a[0]
        # a = a['localId']
        # print("info"+str(a))
        data = {
            "name": name,
            'phone': phone,
            'src_loc': src_loc,
            'des_loc': des_loc,
            'email_address': email_address,
            'pass_number': pass_number,
            'car_number': car_number,
            'day_number': day_number,
            'hr_number': hr_number,
            'car_type': car_type,
            'pickup_place': pickup_place,
            'pickup_hrs': pickup_hrs,
        }
        database.child('reservations').child(millis).set(data)
        # template = loader.get_template('index.html')
        # return HttpResponse(template.render())
        return redirect('/')


# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        src_loc = request.POST.get('src_loc')
        des_loc = request.POST.get('des_loc')
        customer_name = request.POST.get('customer_name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        pass_number = request.POST.get('pass_number')
        car_number = request.POST.get('car_number')
        day_number = request.POST.get('day_name')
        hr_number = request.POST.get('hr_number')
        car_type = request.POST.get('car_type')
        pickup_place = request.POST.get('pickup_place')
        pickup_hrs = request.POST.get('pickup_hrs')

        src_loc1 = request.POST.get('src1_loc')
        des_loc1 = request.POST.get('des1_loc')
        driver_name = request.POST.get('driver_name')
        email_address1 = request.POST.get('email_address1')
        phone_number1 = request.POST.get('phone_number1')
        day_number1 = request.POST.get('day_number1')
        hr_number1 = request.POST.get('hr_number1')
        car_type1 = request.POST.get('car_type1')
        pickup = request.POST.get('pickup')
        ttime = request.POST.get('ttime')
        ddate = request.POST.get('ddate')

        # adding the values in a context variable
        context = {
            'src_loc': src_loc,
            'name': customer_name,
            'email': email_address,
            'phone': phone_number,
            'des_loc': des_loc,
            'pass_number': pass_number,
            'car_number': car_number,
            'day_number': day_number,
            'hr_number': hr_number,
            'car_type': car_type,
            'pickup_place': pickup_place,
            'pickup_hrs': pickup_hrs,

            'src_loc1': src_loc1,
            'des_loc1': des_loc1,
            'driver_name': driver_name,
            'email_address': email_address1,
            'phone_number': phone_number1,
            'day_number1': day_number1,
            'hr_number1': hr_number1,
            'car_type1': car_type1,
            'pickup': pickup,
            'ttime': ttime,
            'ddate': ddate

        }

        # getting our showdata template
        template = loader.get_template('untitled10/index.html')
        # returing the template
        return HttpResponse(template.render(context, request))

    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('untitled10/index.html')
        return HttpResponse(template.render())


def cars(request, template="cars.html"):
    print("cars")
    return render_to_response(template)

def carlist(request):
    template = loader.get_template('carlist.html')
    return HttpResponse(template.render())



def drivers(request, template="drivers.html"):
    return render_to_response(template)


def driverlist(request):
    template = loader.get_template('driverlist.html')
    return HttpResponse(template.render())


@csrf_exempt
def post_drivers(request):
    if request.method == 'POST':
        import time
        from datetime import datetime, timezone
        import pytz
        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))
        print("mili" + str(millis))
        src_loc1 = request.POST.get('src1_loc')
        des_loc1 = request.POST.get('des1_loc')
        driver_name = request.POST.get('driver_name')
        email_address1 = request.POST.get('email_address1')
        phone_number1 = request.POST.get('phone_number1')
        day_number1 = request.POST.get('day_number1')
        hr_number1 = request.POST.get('hr_number1')
        car_type1 = request.POST.get('car_type1')
        pickup = request.POST.get('pickup')
        ttime = request.POST.get('ttime')
        ddate = request.POST.get('ddate')

        data2 = {
            'src_loc1': src_loc1,
            'des_loc1': des_loc1,
            'driver_name': driver_name,
            'email_address1': email_address1,
            'phone_number': phone_number1,
            'day_number1': day_number1,
            'hr_number1': hr_number1,
            'car_type1': car_type1,
            'pickup': pickup,
            'ttime': ttime,
            'ddate': ddate

        }
        database.child('drivers').child(millis).set(data2)
        return redirect('/')
