# ☁️ CloudFileHub

A secure and easy-to-use platform to **upload, manage, and access files** using **AWS S3** and **RDS MySQL**.  
CloudFileHub helps you store files in the cloud while keeping your database in sync.




## 🚀 Features

- 📤 Upload files (JPG, PNG, PDF, TXT) securely to AWS S3  
- 🔍 View uploaded files (coming soon)  
- 🔐 Connection status for **S3** and **RDS MySQL**  
- 🛡️ Secure and lightweight  




## 🛠️ Tech Stack

- **Backend:** Python, Streamlit  
- **Cloud Storage:** AWS S3  
- **Database:** AWS RDS MySQL  
- **Environment Management:** `.env` file & `python-venv`  




## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/CloudFileHub.git
cd CloudFileHub
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a .env file in the root directory with:
```bash
# AWS S3
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
AWS_BUCKET_NAME=your_bucket_name

# RDS MySQL
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=3306
```
### 5️⃣ Run the app
```bash
streamlit run app.py
```

### 📂 Usage

- Open the app in your browser (http://localhost:8501)

- Check the sidebar for connection status

- Upload files using the file uploader

### 🧩 Folder Structure
```bash
CloudFileHub/
├── app.py
├── requirements.txt
├── utils/
│   ├── aws_s3.py
│   └── db_connection.py
├── .env
├── .venv/
└── README.md
```

## 👨‍💻 Author 
- Zain Abbas
- GitHub: https://github.com/zainabbas-se
- LinkedIn: https://www.linkedin.com/in/zainabbas-se/





