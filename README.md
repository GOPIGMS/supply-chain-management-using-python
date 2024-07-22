# Flask Marketplace Application

## Overview

This Flask application serves as a platform for connecting buyers and sellers in a marketplace scenario. It includes functionality for user registration, buyer and seller interfaces, and an admin dashboard.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Twilio Python library (`twilio`)
- MySQL Connector (`mysql-connector-python`)
- A MySQL database server (e.g., MySQL Community Server)

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Install Dependencies:**


3. **Database Setup:**
- Ensure MySQL server is running.
- Create a database named `fruits1` (or adjust `mydb` settings as needed).
- The database structure and tables should be set up according to your application requirements.

4. **Configuration:**
- Open `app.py` and update the MySQL database connection parameters (`host`, `user`, `password`, `database`) in the `mydb` initialization.

5. **Twilio Integration:**
- Obtain Twilio account credentials (`account_sid` and `auth_token`) from the Twilio Console.
- Replace `'xyz'` and `'abc'` with your actual credentials in `app.py` where the Twilio `Client` is initialized.

## Running the Application

To start the Flask application, execute the following command in your terminal:


This will start a development server. Open a web browser and go to `http://localhost:5000/` to access the application.

## Usage


## Contributing

This project is open for contributions. Feel free to fork the repository, make changes, and submit a pull request.


