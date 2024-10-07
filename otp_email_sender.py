import smtplib
import math
import random

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp_message = OTP + " is your OTP"

sender_email = "your_gmail@gmail.com"
app_password = "your_app_password_here"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email, app_password)

emailid = input("Enter your email: ")
s.sendmail(sender_email, emailid, otp_message)
s.quit()

a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please check your OTP again")
