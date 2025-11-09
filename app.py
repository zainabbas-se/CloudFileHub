import streamlit as st
from utils.aws_s3 import test_s3_connection, upload_to_s3
from utils.db_connection import test_db_connection

st.set_page_config(page_title="CloudFileHub", page_icon="☁️")

# ----- Sidebar -----
st.sidebar.title("🔐 Connection Status")

s3_connected = test_s3_connection()
if s3_connected:
    st.sidebar.success("✅ Connected to S3")
else:
    st.sidebar.error("❌ S3 Connection Failed")

db_connected = test_db_connection()
if db_connected:
    st.sidebar.success("✅ Connected to RDS MySQL")
else:
    st.sidebar.error("❌ RDS Connection Failed")

# ----- Main Section -----
st.title("☁️ CloudFileHub")
st.write("Upload and manage your files securely using AWS S3 and RDS.")

uploaded_file = st.file_uploader(
    "📤 Upload a file",
    type=["jpg", "png", "pdf", "txt", "jpeg"]
)

if uploaded_file:
    # Upload file and get pre-signed URL
    file_url = upload_to_s3(uploaded_file)
    if file_url:
        st.success("✅ File uploaded successfully!")
        st.markdown(f"[📎 View File]({file_url})")
    else:
        st.error("❌ Upload failed. Check your S3 connection or IAM permissions.")

st.write("---")
