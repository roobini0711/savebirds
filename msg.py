from flask import Flask, redirect, request, url_for
import os
from twilio.rest import Client
#import math

msg = Flask(__name__)


@msg.route('/success/<name>')
def success(name):
    return 'Thank you for your valuable concern'


@msg.route('/getvalue', methods=['POST', 'GET'])
def getvalue():
    #Frequency_observed = int(request.form['name'])
   if request.method == 'POST':
   	user = int(request.form['nm'])
    	return redirect(url_for('success',name=user))
    	#if user > 894:
    	"""
	print("There's a problem")
	account_sid = 'AC9a3bbfdba519e0d6637669f7b8c741f1'
       auth_token  =   '297f98a4b74ac6db37d6dad9d1be1a6e'
       client = Client(account_sid, auth_token)

       message = client.messages.create(
         body='tumhare tower me problem hai!',
         from_='+12404282609',
         to='+917019929683'
      )
      print(message.sid)
      """
     
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))	
    
if __name__ == '__main__':
    msg.run()
