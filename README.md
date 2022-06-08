# email_sender
Python SMTP email sender 
first import Mailer class from email_sender package
then init class object and pass yandex login and yandex application password into constructor
call .send_message method and pass following arguments: receiver (as list), mail subject and message text as string or html as string
only yandex smtp supported for now

# code example

from email_sender.mailer import Mailer

mailer = Mailer('your_mail@yandex.ru', 'app_password')
mailer.send_message(['receiver@gmail.com', 'receiver2@mail.ru'], 'My mail subject', 'My mail text')
