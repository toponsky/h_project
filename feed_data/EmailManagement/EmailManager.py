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
    
  def _connect(self):
    args = [self.config['sever']]
    args.append(int(self.config['port']))
    self.smtp = smtplib.SMTP_SSL(*args)
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
                name = bag.get('name'),
                color_section = bag.get('color_section')
              )
      
  def _prepare_raw_data_content(self, url, imgUrl, name, colorSection):
    with app.app_context(), app.test_request_context():
      return render_template('email.html',
                url = url,
                img_url = 'https:' + imgUrl,
                name = name,
                color_section = colorSection
              )

  def _prepare_new_bag_raw_data_content(self, url, imgUrl, name, colorSection):
    with app.app_context(), app.test_request_context():
      return render_template('new_bag.html',
                url = config.BASE_URL + url,
                img_url = 'https:' + imgUrl,
                name = name,
                color_section = colorSection
              )


  def sendBag(self, receivers, bag):
    self._connect()
    for to in receivers:
      print("Email: send bag: '{0}' to {1}".format(bag.get('name'), to))
      msg = self._prepare_message(to, "Hermes : {0} is available now".format(bag.get('name')), {'html': self._prepare_content(bag)})
      self.smtp.send_message(msg) 
      print("Email sent successfully") 
      
    self.smtp.quit()  

    return {
              "comment": 'Bag: {0}, send to {1} receiver(s)'.format(bag.get('name'), len(receivers)),
              "to": ', '.join(receivers)
          }

  def sendRawData(self, receivers,  url, imgUrl, name, colorSection):
    self._connect()
    for to in receivers:
      print("Email: send bag: '{0}' to {1}".format(name, to))
      msg = self._prepare_message(to, "Hermes : {0} is available now".format(name), {'html': self._prepare_raw_data_content(url, imgUrl, name, colorSection)})
      self.smtp.send_message(msg) 
      print("Email sent successfully")     
    self.smtp.quit()
    return {
              "comment": 'Bag: {0}, send to {1} receiver(s)'.format(name, len(receivers)),
              "to": ', '.join(receivers)
          }
  def sendNewBagRawData(self, receivers, url, imgUrl, name, colorSection):
    self._connect()
    for to in receivers:
      print("Email: send bag: '{0}' to {1}".format(name, to))
      msg = self._prepare_message(to, "Hermes : NEW BAG '{0}' is available now".format(name), {'html': self._prepare_new_bag_raw_data_content(url, imgUrl, name, colorSection)})
      self.smtp.send_message(msg) 
      print("Email sent successfully")     
    self.smtp.quit()
    return {
              "comment": 'New Bag: {0}, send to {1} receiver(s)'.format(name, len(receivers)),
              "to": ', '.join(receivers)
          }        