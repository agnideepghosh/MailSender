import smtplib
content="Hello World"
username=input("Enter your gmail useername")
sender=username
password=input("Enter your password")
recipient="agnideep22@gmail.com"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()#identify the computer
mail.starttls()#to transprt layer security
mail.login(username, password)
header= 'To:' + recipient + '\n' + 'From: ' \
        + sender + '\n' + 'Subject:testing \n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()

#to make this work please go to the google security link:https://myaccount.google.com/lesssecureapps
#and click allow
