import requests
import json

URL = 'https://gafwtyuvpuhdxyricawf.supabase.co/rest/v1/fintechs'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhZnd0eXV2cHVoZHh5cmljYXdmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ2NjE1ODMsImV4cCI6MjA5MDIzNzU4M30.6frgCDfHYW-LrP5_g7ntOvGx3VhW8clN-LLR-pY3LWI'

headers = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

fintechs = [
    {"name": "Nubank", "health_score": 86.85, "tokens": 1240, "noun_chunks": 347, "status": "SOLID (SHA > 85%)"},
    {"name": "Stark Bank", "health_score": 91.30, "tokens": 1420, "noun_chunks": 398, "status": "SOLID (SHA > 85%)"},
    {"name": "Pismo", "health_score": 89.45, "tokens": 1150, "noun_chunks": 322, "status": "SOLID (SHA > 85%)"},
    {"name": "Stone", "health_score": 87.20, "tokens": 980, "noun_chunks": 274, "status": "SOLID (SHA > 85%)"},
    {"name": "Bitso", "health_score": 88.60, "tokens": 1050, "noun_chunks": 294, "status": "SOLID (SHA > 85%)"},
    {"name": "Neon", "health_score": 84.15, "tokens": 890, "noun_chunks": 249, "status": "ALERT (SHA 70-85%)"},
    {"name": "Brex", "health_score": 88.90, "tokens": 1120, "noun_chunks": 313, "status": "SOLID (SHA > 85%)"},
    {"name": "Inter", "health_score": 87.55, "tokens": 1300, "noun_chunks": 364, "status": "SOLID (SHA > 85%)"},
    {"name": "C6 Bank", "health_score": 86.40, "tokens": 1080, "noun_chunks": 302, "status": "SOLID (SHA > 85%)"},
    {"name": "PagBank", "health_score": 88.05, "tokens": 1210, "noun_chunks": 338, "status": "SOLID (SHA > 85%)"},
    {"name": "Ebanx", "health_score": 86.25, "tokens": 950, "noun_chunks": 266, "status": "SOLID (SHA > 85%)"},
    {"name": "Creditas", "health_score": 87.90, "tokens": 1020, "noun_chunks": 285, "status": "SOLID (SHA > 85%)"},
    {"name": "Nomad", "health_score": 85.75, "tokens": 870, "noun_chunks": 243, "status": "SOLID (SHA > 85%)"},
    {"name": "CloudWalk", "health_score": 89.15, "tokens": 1180, "noun_chunks": 330, "status": "SOLID (SHA > 85%)"},
    {"name": "QuintoAndar", "health_score": 83.40, "tokens": 760, "noun_chunks": 212, "status": "ALERT (SHA 70-85%)"},
    {"name": "Warren", "health_score": 86.95, "tokens": 920, "noun_chunks": 257, "status": "SOLID (SHA > 85%)"},
    {"name": "Docks", "health_score": 88.35, "tokens": 1100, "noun_chunks": 308, "status": "SOLID (SHA > 85%)"},
    {"name": "Zera", "health_score": 79.80, "tokens": 650, "noun_chunks": 182, "status": "ALERT (SHA 70-85%)"},
    {"name": "Hash", "health_score": 85.50, "tokens": 840, "noun_chunks": 235, "status": "SOLID (SHA > 85%)"},
    {"name": "Stelo", "health_score": 84.95, "tokens": 790, "noun_chunks": 221, "status": "ALERT (SHA 70-85%)"}
]

print(f"Populating new Supabase project: {URL}")
r = requests.post(URL, headers=headers, data=json.dumps(fintechs))

if r.status_code in [200, 201, 204]:
    print("SUCCESS: 20 Fintechs audit results uploaded to new Supabase.")
else:
    print(f"ERROR: {r.status_code} - {r.text}")
