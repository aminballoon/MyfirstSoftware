import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('software-development-a113f-firebase-adminsdk-8c482-40856bccf8.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

^   ^
|   |
|   |
|   |

เอาไว้เข้าถึง firebase