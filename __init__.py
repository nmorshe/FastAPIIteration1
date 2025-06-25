import os
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TYPE = os.getenv('FASTAPI_FIREBASE_TYPE')
PROJECT_ID = os.getenv('FASTAPI_FIREBASE_PROJECT_ID')
API_KEY_ID = os.getenv('FASTAPI_FIREBASE_API_KEY_ID')
PRIVATE_API_KEY = os.getenv('FASTAPI_FIREBASE_PRIVATE_API_KEY')
CLIENT_EMAIL = os.getenv('FASTAPI_FIREBASE_CLIENT_EMAIL')
CLIENT_ID = os.getenv('FASTAPI_FIREBASE_CLIENT_ID')
AUTH_URI = os.getenv('FASTAPI_FIREBASE_AUTH_URI')
TOKEN_URI = os.getenv('FASTAPI_FIREBASE_TOKEN_URI')
AUTH_PROVIDER_CERT = os.getenv('FASTAPI_FIREBASE_AUTH_PROVIDER_CERT')
CLIENT_PROVIDER_CERT = os.getenv('FASTAPI_FIREBASE_CLIENT_PROVIDER_CERT')
UNIVERSE_DOMAIN = os.getenv('FASTAPI_FIREBASE_UNIVERSE_DOMAIN')

FIREBASE_CRED = {
  "type": TYPE,
  "project_id": PROJECT_ID,
  "private_key_id": API_KEY_ID,
  "private_key": PRIVATE_API_KEY,
  "client_email": CLIENT_EMAIL,
  "client_id": CLIENT_ID,
  "auth_uri": AUTH_URI,
  "token_uri": TOKEN_URI,
  "auth_provider_x509_cert_url": AUTH_PROVIDER_CERT,
  "client_x509_cert_url": CLIENT_PROVIDER_CERT,
  "universe_domain": UNIVERSE_DOMAIN
}