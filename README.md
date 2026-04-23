# CreditRate Login Dashboard

## Overview
This project is an enhanced version of the CreditRate dashboard, featuring a secure login system. It allows authorized users to view analytics regarding company credit rates stored in a CSV database.

## Key Features
- **Authentication**: Secure login gateway (Default credentials: `admin` / `1234`).
- **Session Management**: Uses Flask sessions to protect the dashboard route.
- **In-Memory Chart Generation**: Generates Matplotlib charts and serves them directly as Base64 strings, avoiding unnecessary disk I/O.
- **Responsive Dashboard**: Displays a bar chart of company counts grouped by credit rate.

## Tech Stack
- **Backend**: Python, Flask
- **Data Analysis**: Pandas
- **Visualization**: Matplotlib
- **Frontend**: HTML/CSS

## Setup Instructions
1. Install the required Python packages:
   ```bash
   pip install flask pandas matplotlib
   ```
2. Ensure your data is located at `data/customers.csv`.
3. Start the Flask server:
   ```bash
   python app.py
   ```
4. Log in at `http://localhost:5000` using the provided credentials.
