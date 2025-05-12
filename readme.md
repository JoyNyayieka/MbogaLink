# 🛒 MbogaLink

##  Project Overview

This project is a Django-based e-commerce platform tailored for small-scale fresh produce vendors. It enables vendors to list their products, manage inventory, and receive payments, while customers can browse nearby vendors, view fresh produce, and place orders. 

The platform is optimized for accessibility and ease of use, especially for users with limited technical expertise, and it aims to bridge the digital gap in informal markets by offering a lightweight, mobile-friendly solution.

---

##  Key Features

| Feature                             | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
|  Vendor Dashboard                 | Allows vendors to upload products, manage listings, and view orders.        |
|  Customer Interface             | Customers can browse produce, add to cart, and place orders.                |
|  Secure Payments                 | Integrated payment API for real-time and secure transactions.               |
|  Location-Based Discovery         | Customers find nearby vendors using location filters.                       |
|  Responsive Design                | Bootstrap-powered interface ensures mobile-friendliness.                    |
|  Authentication                   | Login system for vendors and customers with secure credential handling.     |

---

##  Technologies Used

| Category            | Tools/Technologies                               |
|---------------------|---------------------------------------------------|
|  Backend            | Python, Django, SQLite3                           |
|  Frontend           | HTML, CSS, Bootstrap Template (customized)       |
|  Testing            | Django Test Framework                            |
| Payment Integration| Daraja API (M-Pesa)           |
|  Dev Tools        |  PyCharm, Git, Virtualenv     |

---

##  How to Run the Project

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/fresh-produce-platform.git
cd fresh-produce-platform
```
2. **Set Up the virtual environment**
```commandline
python -m venv venv
source venv/bin/activate 
```
3. **Install dependancies**
```commandline
pip install -r requirements.txt
```
4. **Run Migrations**
```commandline
python manage.py migrate
```
5. **Create a superuser**
```commandline
python manage.py createsuperuser
```
6. **Run the development server**
```commandline
python manage.py runserver
```

## Future Improvements
🌐 Multi-language Support to cater to diverse communities.

📦 Logistics Module for tracking deliveries and linking riders.

📊 Analytics Dashboard for vendors to track sales and trends.

📱 Android/iOS App version using React Native or Flutter.

## Known Limitations
- SQLite3 is not optimal for high-concurrency; upgrading to PostgreSQL is recommended for production.
- Real-time notifications and delivery tracking are not yet implemented.

## Author
[Joy Nyayieka](https://www.linkedin.com/in/joynyayieka/)