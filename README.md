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
**Set the FLASK_APP environment variable**:
   
   If your Flask app is in a file named `app.py`, set the environment variable as follows:

   - On macOS/Linux:
     ```bash
     export FLASK_APP=app.py
     ```

   - On Windows:
     ```cmd
     set FLASK_APP=app.py
     ```


This will start a development server. Open a web browser and go to `http://localhost:5000/` to access the application.


## Endpoints

### Homepage

- **URL:** `/`
- **Description:** Main landing page of the application.

### Buyer

- **URL:** `/buyer`
- **Description:** Interface for buyers to view products or services.

### Seller

- **URL:** `/seller`
- **Description:** Interface for sellers to manage their listings.

### Admin

- **URL:** `/admin`
- **Description:** Dashboard for admin tasks and management.

### Buyer Registration

- **URL:** `/buy_reg`
- **Description:** Form for buyers to register.

### Seller Registration

- **URL:** `/sell_reg`
- **Description:** Form for sellers to register.


### Buyer Validation

- **URL:** `/buyerval`
- **Methods:** `POST`, `GET`
- **Description:** Handles the validation of buyers. On POST request, retrieves the `username` and `password` from the form data.

### Seller Validation

- **URL:** `/sellerval`
- **Methods:** `POST`, `GET`
- **Description:** Handles the validation of sellers.

### Admin Validation

- **URL:** `/adminval`
- **Methods:** `POST`, `GET`
- **Description:** Handles the validation of admins. On POST request, retrieves the `username` and `password` from the form data.

### Seller Dashboard

- **Function:** `sell_dash()`
- **Description:** Retrieves the balance of the seller from the database.

### Purchase

- **URL:** `/purchase`
- **Methods:** `POST`, `GET`
- **Description:** Handles product purchases. On POST request, retrieves the `product` from the form data.

### Add Product

- **URL:** `/add_prod`
- **Methods:** `POST`, `GET`
- **Description:** Handles the addition of new products by sellers. On POST request, retrieves various product details from the form data.

### Account Details

- **URL:** `/acc_details`
- **Methods:** `POST`, `GET`
- **Description:** Handles the account details of users. On POST request, retrieves account details from the form data.

### Seller Account

- **URL:** `/sell_acc`
- **Description:** Retrieves details of the seller from the database.

### View Products

- **URL:** `/view`
- **Description:** Retrieves and displays products of a specific seller from the database.

### Seller Details

- **URL:** `/sell_detail`
- **Description:** Retrieves and displays details of all sellers from the database.

## Notes 

- Make sure to handle sessions and database connections securely.
- Ensure proper validation and error handling for all form inputs and database operations.


## Contributing 

This project is open for contributions. Feel free to fork the repository, make changes, and submit a pull request.


