# import sys
# sys.path.insert(0, '../src')
# from src.view.view import View
from src.service.template import ViewTemplate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("EMAIL_PASSWORD")

view_template = ViewTemplate()

class Mail:
    def send_mail(self, login_user, name_user, email_to, template_path):
        body_template = view_template.message(login_user, name_user, template_path)
        message = MIMEMultipart()
        message['from'] = 'Admin Backend'
        message['to'] = email_to
        message['subject'] = 'Assunto Liga da Justiça'

        body = MIMEText(body_template, 'html')
        message.attach(body)
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login('wag.backend@gmail.com', PASSWORD)
                smtp.send_message(message)
                print('E-mail enviado com sucesso.')
            except Exception as e:
                print('E-mail não enviado...')
                print('Erro:', e)

# if __name__ == '__main__':
    # send = Mail()

    # template_path_welcome = 'src/template/template_welcome.html'
    # template_path_welcome_confirm = 'src/template/template_confirm_email.html'
    # send.send_mail('Flash', 'Barry', 'wag.backend@gmail.com', template_path_welcome_confirm)
