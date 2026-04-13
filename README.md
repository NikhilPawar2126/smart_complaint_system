# Smart Complaint & Service Management System

A professional, full-stack web application designed for users to submit, manage, and track complaints or service requests. It features a modern, responsive user interface built with Tailwind CSS and a robust backend powered by Python, Flask, and SQLite.

## ✨ Features

### For Users:
- **User Authentication:** Secure registration and login flow.
- **Submit Complaints:** Easily file new complaints with a title, description, category, and an optional image attachment.
- **Track Status:** View all submitted complaints and their current status (Pending, In Progress, Resolved).
- **Responsive Dashboard:** A clean, tailored dashboard for an optimal user experience across all devices.

### For Administrators:
- **Admin Dashboard:** A centralized control panel for managing all system complaints.
- **Update Status:** Instantly update complaint statuses (e.g., mark as "In Progress" or "Resolved").
- **Filtering & Analytics:** Filter complaints by status or category and view overall system metrics.
- **Image Handling:** View securely uploaded attachments associated with complaints.

## 🛠️ Technology Stack

- **Backend Framework:** Python (Flask)
- **Database:** SQLite (managed via Flask-SQLAlchemy)
- **Authentication:** Flask-Login & Werkzeug Security
- **Frontend Styling:** Tailwind CSS 
- **Template Engine:** Jinja2

## 📂 Project Structure

```text
smart_complaint_system/
│
├── app.py                  # Main application entry point & configuration
├── models.py               # Database models (User, Complaint)
├── requirements.txt        # Python dependencies
├── instance/               # Contains the SQLite database file (database.db)
├── static/                 # Static assets
│   └── uploads/            # Directory for user-uploaded images
├── templates/              # HTML/Jinja2 templates
│   ├── base.html           # Base layout template
│   ├── index.html          # Landing page
│   ├── login.html          # User/Admin login page
│   ├── register.html       # User registration page
│   ├── dashboard.html      # User dashboard
│   ├── submit_complaint.html # Complaint submission form
│   └── admin_dashboard.html  # Administrator dashboard
└── routes/                 # Separated route handling (Blueprints)
    ├── auth_routes.py      # Authentication routes (login, register, logout)
    ├── user_routes.py      # User specific routes (dashboard, new complaint)
    └── admin_routes.py     # Admin specific routes (manage complaints)
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+ installed on your system.

### 1. Clone or Download the Repository
Navigate to your desired folder and open a terminal.

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Start the Flask development server. This step will also automatically initialize the SQLite database and create the default admin user.
```bash
python app.py
```

### 6. Access the Application
Open your web browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🔐 Default Admin Credentials

When the application runs for the first time, it automatically creates a default administrator account.

- **Email:** `admin@system.com`
- **Password:** `admin123`

*(Note: Please ensure you change these credentials or handle them securely before deploying to a production environment.)*

## 💡 Usage Workflow

1. Navigate to the landing page and register a new user account.
2. Log in with your new credentials to access the user dashboard.
3. Submit a new complaint, providing an optional image.
4. Log out, and then log back in using the **Admin Credentials** provided above.
5. Access the Admin Dashboard to review the submitted complaint and update its status.
