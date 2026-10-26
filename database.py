
import streamlit as st
from supabase import create_client


def get_supabase_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_SECRET_KEY"]
    return create_client(url, key)


def test_database_connection():
    try:
        client = get_supabase_client()
        response = (
            client.table("care_records")
            .select("id")
            .limit(1)
            .execute()
        )
        return True, "Supabase connection successful."
    except Exception as exc:
        return False, f"Supabase connection failed: {exc}"
