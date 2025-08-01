from fastapi import FastAPI
from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

@app.get("/insurers")
def get_insurers():
    res = supabase.table("insurer_info").select("*").execute()
    return res.data
insurers_data=get_insurers()

print(insurers_data)