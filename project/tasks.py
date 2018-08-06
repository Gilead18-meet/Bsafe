from celery import Celery
from twilio.rest import Client
import time

#Georges's phone:
ACC_SID = "ACd03777f4973c4f1ffc3efed677cc57b1"
AUTH_TOKEN = "b22f0d66110237b42ebf63ccd2b4241e"
FROM = "+18482088916"
BODY = "YOUR BABY MIGHT BE IN DANGER! CHECK YOUR CAR!"


app = Celery('tasks', broker='redis://localhost' )

@app.task(bind = True)
def alert(self, number, flag, phone1, phone2, phone3):
	print('hereWEASDADASDJKASLDJASKLDJSAKLDJASKLDJASKLDJASKLDJASKLDJASDKLKASDJASKDLK')
	dest = number
	while True:
		client = Client(ACC_SID, AUTH_TOKEN)
		if flag == 2 and phone1:
			dest = phone1
		elif flag == 3 and phone2:
			dest = phone2
		elif flag == 4 and phone3:
			dest = phone3
		elif flag == 5:
			flag = 0
			break 
		client.messages.create(to=dest, from_=FROM, body=BODY+' '+str(self.request.id))
		flag+=1
		print (flag)
		print ('FLAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG') 
		time.sleep(30)
	return 

def revoke(task_id):
	app.control.revoke(task_id, terminate=True)