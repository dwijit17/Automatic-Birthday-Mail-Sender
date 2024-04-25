import os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
#Getting the current date 
date = datetime.now().date()
date = str(date)
date = date[5:]
#Reading the Birthdays File
Birthdays = pd.read_excel('Birthdays.xlsx')
#Reading the Birthdays and if day matches with today
#we send and email to them wishing birthday
email = os.environ.get('EMAIL')
pwd = os.environ.get('PWD')

def sendWishes(receiver_email):
    msg = MIMEMultipart('alternative')
    # Create the HTML part of the message.
    html_content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap">
  <title>Happy Birthday card || Learningrobo</title>
  <style>
  
* {
  transition: all 0.2s ease-in-out;
}

body {
  background: #DCE35B; 
background: -webkit-linear-gradient(to right, #45B649, #DCE35B); 
background: linear-gradient(to right, #45B649, #DCE35B); 
  display: grid;
  place-items: center;
  height: 100vh;
  margin: 0;
  font-family: 'Open Sans', sans-serif;
}

.card {
  background: #12192c;
  border-radius: 30px;
  height: 85vh;
  width: 80vw;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1em;
  overflow: hidden;
  color:#DCE35B;
}

@media only screen and (min-width: 1000px) {
  .card {
    flex-direction: row-reverse;
  }
  .card img.birthday {
    width: 60%;
    max-width: 50vw;
    max-height: unset;
    border-radius: 30px;
  }
}

@media only screen and (max-height: 640px) {
  .card {
    flex-direction: row-reverse;
  }
  .card img.birthday {
    width: 100%;
    max-width: 50vw;
    max-height: unset;
  }
}

img.birthday {
  max-height: 40vh;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}

.text {
  padding: 3em;
}
.text h1{
  font-family:cursive;
  font-size: 40px;
}
.space {
  height: 100px;
}

.credit a{
  text-decoration: none;
  color: #fff;
}

.credit {
    margin-top: 10px;
    text-align: center;
}


  </style>
</head>
<body>
  <div class="card">
    <img src="https://cdn.pixabay.com/photo/2020/10/06/21/54/cake-5633461__480.png" alt="birthday" class="birthday">
    <div class="text">
      <h1>Happy Birthday!</h1>
      <p>Have a great future..!</p>
      <p>- Dwijit Dasari</p>
      <div class="credit">Made with <span style="color:tomato">❤</span> by <a  href="https://www.learningrobo.com/">Dwijit</a></div>
    </div>
    <div class="space"></div>
  </div>
</body>
</html>
    '''
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)
    try:
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(email,pwd)
        s.sendmail(email,receiver_email,msg.as_string())
        s.quit()
    except Exception as e:
        print('An Error has Occured',e)

sno=0
for ele in Birthdays['DOB']:
    bday = str(ele)
    bday = bday[5:10]
    receiver = Birthdays['Email'][sno]
    if(bday == date):
        sendWishes(receiver_email=receiver)
    sno+=1

