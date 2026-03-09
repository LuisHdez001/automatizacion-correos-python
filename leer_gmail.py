import os.path
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle

# permiso SOLO lectura
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = None

# guarda sesión para no pedir login siempre
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credenciales.json', SCOPES)
    creds = flow.run_local_server(port=0)

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

# leer últimos correos
results = service.users().messages().list(userId='me', maxResults=5).execute()
messages = results.get('messages', [])

print("Correos encontrados:", len(messages))