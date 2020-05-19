from django.shortcuts import render,HttpResponse
import qrcode
from user.models import user_profile
from .models import gate_entry
import datetime
from django.contrib.auth.decorators import login_required



# this function will generate qr containing passed data
def generate_qr(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 5,
        border = 1,
    )
    user_data = "{};{};{};{};".format(data['regno'],data['user'],data['roomno'],data['profile_url'])
    qr.add_data(user_data)
    qr.make(fit=True)
    img = qr.make_image()
    print('inside qr functioooooo')
    
    # img.save('image.jpg')
    img.save("static/qr/{}.jpg".format(data['regno']))
  
@login_required
def generate_qr_view(request):
    
    user = user_profile.objects.filter(user = request.user)
    user_profile_pic_url = user[0].profile_pic.url
    # print(user_profile_pic_url)
    user_details = {
        'user':user[0].user,
        'regno':user[0].regno,
        'roomno':user[0].roomno,
        'firstname':user[0].user.first_name,
        'profile_url':user_profile_pic_url
    }
    #this will generate a qr code image
    generate_qr(user_details)
    
    
    return render(request,'qr/code.html',{
        'qr_url':"/static/qr/{}.jpg".format(user_details['regno']),
        'profile_pic_url':user_profile_pic_url,
        'regno':user_details['regno']
        })