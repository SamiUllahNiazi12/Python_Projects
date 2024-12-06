import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('samiuallahkhaniazi@gmail.com','samikhan1212')
subject = "test python"
body = "I love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['prajapatgaurav08@gmail.com',
           'prajapatgaurav601@gmail.com']

ob.sendmail('samiuallahkhaniazi@gmail.com',listadd,message)
print("send mail")
ob.quit()
