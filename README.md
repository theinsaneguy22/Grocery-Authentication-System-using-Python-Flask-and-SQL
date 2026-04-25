# Grocery Authentication System (Backend Project)

A backend-focused web application that implements a user authentication system using Flask and MySQL. The project demonstrates how user data is stored, validated, and managed through session-based authentication.
This project focuses on user registration, login validation, session handling, and database integration, forming the foundation of secure web applications.

# 💻 Technologies Used
- Python
- Flask
- MySQL
- Jinja2 Templates
- HTML / CSS (for basic UI rendering)


# 🔄 Flow of Project

User Registration → Data Stored in MySQL → Login Request → Credential Validation → Session Creation → Access Protected Route → Logout & Session Removal

# 🚀 Project Features

  # 1. User Registration
  - Users can register with username and password
  - Data stored in MySQL database (users table)
  
  # 2. Login Authentication
  - Validates user credentials from database
  - Allows access only if credentials are correct
  
  # 3. Session Management
  - Flask sessions used to maintain login state
  - Protected routes accessible only after login
  - Session cleared on logout
  
  # 4. Protected Routes
  - home route accessible only to logged-in users
  - Unauthorized users are redirected to login page
  
  # 5. Database Integration
  - MySQL used for storing user data
  - Demonstrates backend-to-database interaction
  
  # 6. API Testing (Postman)
  - Login and register routes tested using Postman
  - Verified backend functionality independently

# 📊 Key Learning Outcomes
- Authentication system design
- Session handling in Flask
- Backend development with Flask
- MySQL database integration
- Route protection and access control

# 📌 Future Enhancements
- Password hashing for security
- Token-based authentication (JWT)
- Role-based access control
- API-only architecture
