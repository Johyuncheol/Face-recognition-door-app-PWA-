import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import sys


cred_path = "lock-2674d-firebase-adminsdk-1vxls-912772558b.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = 'cQiFE9KGR8KLkI0lwaJMqW:APA91bGQTj5yyRVv5FmcwnKB3LDqcc-DNskcq596i6gRBnjJ0gkscv1Tn3QgYfWJJUq3OePCNz9nkzZLpXTWHHwFfWJp9IUbYqLA1hCFTpTM_Ugthl7hW7sDUmi81BxdjEzRrVjTxyAj'
message = messaging.Message(
    notification = messaging.Notification(
        title = '문앞에 누가 왔어요 !',
        body='문을 열까요?'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)
sys.exit(0)