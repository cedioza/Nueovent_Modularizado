
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config

def sendEmail(email,name,case):
  
  if case==1:
    subject=f'Bienvenido a Nuovent {name} '
    content='<strong>Bienvenido  ahora podras crear nuevos anuncios o alojamientos </strong>'
  else:
   subject=f'Nuevo anuncio creado'
   content=f'<strong> Se creo un nuevo anuncio {name} </strong>'

  message = Mail(
    from_email='cedioza@gmail.com',
    to_emails=email,
    subject=subject,
    html_content=content)
  try:
      sg = SendGridAPIClient(config('KEY_SENDGRID'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(e)
