A simple Python script that generates a 6-digit OTP (One-Time Password) and sends it via email using Gmail's SMTP service. The script allows users to input their email address, receive the OTP, and verify it for confirmation.

Features
Generates a 6-digit OTP.
Sends the OTP to the provided email address.
Verifies the entered OTP against the generated one.
Requirements
Make sure you have Python 3.x installed on your machine.

To install the necessary dependencies, you can use:
![image](https://github.com/user-attachments/assets/2f3ad8b5-54e8-4c7b-a1da-0a1abd2e8f7b)
Google App Password Setup
If you have 2-Step Verification enabled on your Google account, you'll need to generate an App Password to use in this script. Here's how to do it:

Go to your Google Account Security Page.
Under "Signing in to Google," make sure 2-Step Verification is enabled.
Once enabled, you’ll see a section for App Passwords. Click on it.
Select Mail from the drop-down menu and choose your device (or select Other to name it something like "OTP Email Sender").
Click Generate. Google will show you a 16-character password.
Copy this password and replace your_app_password_here in the code with the generated password.
Setup
Clone the Repository:
![image](https://github.com/user-attachments/assets/aa1c5799-f1c0-4830-8240-0e62fad922d9)
Environment Variables (Optional but recommended):

Store your Gmail credentials in an .env file to avoid hardcoding sensitive information.
Example .env:
![image](https://github.com/user-attachments/assets/97d8a65d-b7d1-4866-aa34-ffaf145739ee)
Run the Script:
![image](https://github.com/user-attachments/assets/1a38a141-4b27-453e-b675-97b5efb4dac4)
Usage
Enter your email address when prompted.
The script will send a 6-digit OTP to the provided email.
Enter the OTP you received to verify it.
If the OTP is correct, you will see the message "Verified." Otherwise, it will ask you to check your OTP again.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Contact
For any inquiries, you can reach me at boobeshganesan@gmail.com.


