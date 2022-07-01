import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "test-firebase-adminsdk-enmn8-121aaec091.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = 'cBPtDKvuSBK1C7jsu9j5Tk:APA91bE52VQRECUCAILH4XVmLcmMuISbV9QTHZgr3II_03cbuSha9a-MBl5xgop9jlQ6-tSdBRumj5zu8pdwCgvK2ySQXt-RMTQveK34pQjSePRf8TkBtrKDpRK6r27dpPzwA0pSSLIM'
message = messaging.Message(
    notification = messaging.Notification(
        title='title',
        body='body'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)