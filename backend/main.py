from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

@app.get("/users")
def get_users():
    res = supabase.table("users").select("*").execute()
    return res.data
