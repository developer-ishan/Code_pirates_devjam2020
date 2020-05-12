from django.shortcuts import render,HttpResponse
import qrcode
from user.models import user_profile
from .models import gate_entry
import datetime



# this function will generate qr containing passed data
def generate_qr(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 5,
        border = 1,
    )
    user_data = "Name:{}\nRegistration_no:{}\nRoom_No.:{}\nProfile_url:{}".format(data['user'],data['regno'],data['roomno'],data['profile_url'])
    qr.add_data(user_data)
    qr.make(fit=True)
    img = qr.make_image()
    print('inside qr functioooooo')
    
    img.save('image.jpg')
    # img.save("/static/images/qr/{}.jpg".format(data['regno']))
  

#this function will create a gate entry
def create_gate_entry(user_details):
    
    #this will only get the unclosed entry not the closed one by a regno
    previous_entry = gate_entry.objects.filter(regno = user_details['regno'],intime = None)
    now=datetime.datetime.now()
    if previous_entry:
        # previous_entry.intime = now
        previous_entry.update(intime = now)
    else:
        name = user_details['firstname']
       
        # printname = print(user_details['user'])
        # print(printname)
        gate_entry.objects.create(name = name,regno = user_details['regno'],roomno = user_details['roomno'],outtime = now)

def generate_qr_view(request):
    
    user = user_profile.objects.filter(user = request.user)
    # user_profile_pic_url = user[0].profile_pic.url
    # print(user_profile_pic_url)
    user_details = {
        'user':user[0].user,
        'regno':user[0].regno,
        'roomno':user[0].roomno,
        'firstname':user[0].user.first_name,
        'profile_url':user[0].profile_pic.url
    }
    #this will generate a qr code image
    print('generating qr.....')
    generate_qr(user_details)
    print('qr generated')
    create_gate_entry(user_details)
    
    return render(request,'qr/code.html',{
        'qr_url':"/static/images/qr/{}.jpg".format(user_details['regno']),
        'profile_pic_url':user_profile_pic_url
        })