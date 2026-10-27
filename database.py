
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
            "content": {"observation": "Temporary test record"},
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
        return bool(fetched.data), "Database write/read/delete test completed."
    except Exception as exc:
        return False, f"Database test failed: {exc}"


def save_observation_to_db(observation, mood=""):
    record = {
        "record_type": "observation",
        "content": {"observation": observation, "mood": mood},
    }
    return (
        get_supabase_client()
        .table("care_records")
        .insert(record)
        .execute()
    )


def get_observations_from_db(limit=50):
    response = (
        get_supabase_client()
        .table("care_records")
        .select("id, content, created_at")
        .eq("record_type", "observation")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return response.data


def save_task_to_db(task):
    client = get_supabase_client()
    record = {
        "record_type": "task",
        "content": task,
    }
    return client.table("care_records").insert(record).execute()


def save_alert_to_db(alert):
    client = get_supabase_client()
    record = {
        "record_type": "alert",
        "content": alert,
    }
    return client.table("care_records").insert(record).execute()
