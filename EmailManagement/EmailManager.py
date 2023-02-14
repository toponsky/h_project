import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template

import config

app = Flask(__name__)

@app.route('/EmailManagement')
class EmailManager:
  def __init__(self, smtp_config):
    self.config = smtp_config
    smtp_class = smtplib.SMTP_SSL
    args = [self.config['sever']]
    args.append(int(self.config['port']))
    self.smtp = smtp_class(*args)
    self.smtp.login(self.config['username'], self.config['password'])
    


  def _prepare_message(self, send_to, subject, contents):

      msg = MIMEMultipart()
      msg.set_charset('utf-8')

      msg['To'] = send_to
      msg['From'] = 'toponsky@irishdata.ie'
      msg['Subject'] = subject

      body = MIMEMultipart('alternative')

      if contents.get('plaintext'):
          body.attach(MIMEText(contents['plaintext'], 'plain', 'utf-8'))

      if contents.get('html'):
          body.attach(MIMEText(contents['html'], 'html', 'utf-8'))

      msg.attach(body)

      return msg  

  def _prepare_content(self, bag):
    with app.app_context(), app.test_request_context():
      return render_template('email.html',
                url = config.BASE_URL + bag.get('url'),
                img_url = 'https:' + bag.get('img_url'),
                name = bag.get('name')
              )
      

  def sendEmail(self, bag):
    for to in self.config['to']:
      print("Email: send bag: '{0}' to {1}".format(bag.get('name'), to))
      msg = self._prepare_message(to, "Hermes Available Bag", {'html': self._prepare_content(bag)})
      self.smtp.send_message(msg) 
      print("Email sent successfully") 

  