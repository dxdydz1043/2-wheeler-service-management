import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'prsontester@gmail.com'
    msg['from'] = user
    password = 'fvdvzjsaunytljon'

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert('Hi',"Your requested Services have been completed","custmailssn@gmail.com")