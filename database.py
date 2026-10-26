
import streamlit as st
from supabase import create_client


def get_supabase_client():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_SECRET_KEY"],
    )


def test_database_connection():
    try:
        client = get_supabase_client()
        client.table("care_records").select("id").limit(1).execute()
        return True, "Supabase connection successful."
    except Exception as exc:
        return False, f"Supabase connection failed: {exc}"


def test_database_write_read():
    try:
        client = get_supabase_client()
        sample = {
            "record_type": "observation",
            "content": {"observation": "Sample test record - safe to delete"},
        }
        inserted = client.table("care_records").insert(sample).execute()
        record_id = inserted.data[0]["id"]

        fetched = (
            client.table("care_records")
            .select("id, content")
            .eq("id", record_id)
            .single()
            .execute()
        )

        client.table("care_records").delete().eq("id", record_id).execute()

        if fetched.data:
            return True, "Database write/read/delete test successful."
        return False, "Record was inserted but could not be retrieved."
    except Exception as exc:
        return False, f"Database test failed: {exc}"
