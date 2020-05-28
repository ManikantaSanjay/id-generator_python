from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (135, 206, 250))
#Light Sky Blue Code is choosen for Image Bg Color,with dimensions 1000*900
draw = ImageDraw.Draw(image)

#For linux check your installed font from fc-list
#or install it using "apt-get install fontconfig" for ubuntu and select one from it.


font = ImageFont.truetype('arial.ttf', size=45)
import random
import os,sys
import datetime
import qrcode
import datetime
os.system("ID CARD Generator")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
 
# starting position of the message
print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(255, 255, 255)'
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)


# adding an unique id number. You can manually take it from user
(x, y) = (620, 75)
idno=random.randint(10000000,90000000)
message = str('ID No:'+str(idno))
color = 'rgb(255, 255, 255)' # white color
font = ImageFont.truetype('arial.ttf', size=50)
draw.text((x, y), message, fill=color, font=font)




(x, y) = (50, 200)
message = input('Enter Your Full Name: ')
name=message
name1='Name:'+message
color = 'rgb(0, 0, 0)' # black color
font1 = ImageFont.truetype('C:/Windows/Fonts/Verdana.ttf', size=40)
draw.text((x, y), name1, fill=color, font=font1)



(x, y) = (50, 300)
message = input('Enter Your Gender: ')
temp='Gender:'+message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), temp, fill=color, font=font1)



(x, y) = (50, 400)

isValidDate = False
while(isValidDate == False):
    message = input("Enter the date in format 'dd-mm-yyyy' : ")
    try:
        day,month,year = message.split('-')
        datetime.datetime(int(year),int(month),int(day))
        isValidDate = True
    except ValueError :
        isValidDate = False
        print('Please,Enter Correct Date of Birth in dd-mm-yyyy format')

year=message
mssg='Date Of Birth:'+message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), mssg, fill=color, font=font1)

(x,y) = (50,500)
y1 =  year.split('-')
present_year=int(2020)
age = present_year - int(y1[2])
message1 =  "Age:" + str(age)
draw.text((x, y), message1, fill=color, font=font1)






bloodgroup=['a-ve','a+ve','a+ve','a-ve','b-ve','b+ve','ab+ve','ab-ve','o+ve','o-ve','opositive','onegative','o-ve'
'apositive','anegative','bnegative','bpositive','abpositive','abnegative']
(x, y) = (50, 600)
bg = False
while(bg==False):
    message = input("Enter bloodgroup:")
    string2=message.lower().replace(" " ,"")
    if string2 in bloodgroup:
        bg=True
    else:
        print('Enter Valid Blood Group') 
 
        
color = 'rgb(255, 0, 0)' # black color 
temp = 'Blood Group:' + message.upper()
draw.text((x, y), temp, fill=color, font=font1)



(x, y) = (50, 700)
mobileno=False
while(mobileno==False):
    count=0
    message = input('Enter Your Mobile Number: ')
    mssg=int(message)
    while(mssg>0):
        mssg=mssg//10
        count=count+1
    if(count==10):
        mobileno=True
    else:
        print('Enter Valid Mobile Number consisting of 10 digits')            
    
    
temp='Mobile Number:'+ message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), temp, fill=color, font=font1)




(x, y) = (50, 800)
addr=False
while(addr==False):
    message = input('Enter Your Address: ')
    if(message==''):
        print('Address cannot Be Empty')
    else:
        addr=True    
temp = 'Address:'+message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), temp, fill=color, font=font1)




# save the edited image
 
image.save(str(name)+'.png')

mywidth = 300

img = Image.open('profile.png')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), Image.ANTIALIAS)
img.save('resized.jpg')




til = Image.open(name+'.png')
im = Image.open('resized.jpg') 
til.paste(im,(650,200))
til.save(name+'.png')

img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
img.save(str(idno)+'.bmp')
til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp') #25x25
til.paste(im,(650,550))
til.save(name+'.png')
print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))
eval(input('\n\nPress any key to Close program...'))