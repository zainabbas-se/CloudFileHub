# ☁️ CloudFileHub

A secure and easy-to-use platform to upload, manage, and access files using AWS S3 and RDS MySQL. CloudFileHub helps you store files in the cloud while keeping your database in sync.

---

## 🚀 Features

- Upload files (JPG, PNG, PDF, TXT) securely to AWS S3
- Track uploaded files in RDS MySQL
- Sidebar connection status for S3 and MySQL
- Easy retrieval of uploaded files (coming soon)
- Simple, responsive Streamlit interface

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
~~~bash
git clone https://github.com/your-username/CloudFileHub.git
cd CloudFileHub
~~~

### 2️⃣ Create a virtual environment
~~~bash
python -m venv .venv
~~~

### 3️⃣ Activate the virtual environment

- Windows:
  ~~~bash
  .venv\Scripts\activate
  ~~~

- macOS / Linux:
  ~~~bash
  source .venv/bin/activate
  ~~~

### 4️⃣ Install dependencies
~~~bash
pip install -r requirements.txt
~~~

### 5️⃣ Set up environment variables

Create a `.env` file in the project root with the following content:

~~~env
# AWS S3
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
AWS_BUCKET_NAME=cloud-file-hub

# RDS MySQL
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=3306
~~~

---

## 💡 How It Works

1. The Streamlit app initializes and checks connections to S3 and RDS.
2. Users upload files through the UI.
3. Files are uploaded to S3 using boto3.
4. Uploaded files are tracked in the database and can be retrieved later.

---

## 👨‍💻 Author

- Zain Abbas  
- GitHub: https://github.com/zainabbas-se  
- LinkedIn: https://www.linkedin.com/in/zainabbas-se/