# Moci Petshop - Custom Odoo 16 ERP Module

A custom Odoo 16 module developed to manage the daily operations of Moci Petshop. This module handles pet data management and grooming services, featuring direct integration with Odoo's native Sales module.

This project was built to demonstrate a practical understanding of ERP concepts, business logic implementation, and Python development for Odoo.

## 🌟 Key Features

1. **Custom Data Models (Python & PostgreSQL)**
   - `moci.pet`: Manages pet profiles (Name, Species, Breed, Medical Notes).
   - `moci.grooming`: Manages grooming service transactions (Service Type, Date, Price, Status).
   - Establishes a `Many2one` relational database connection with Odoo's native customer data (`res.partner`).

2. **Custom Views (XML)**
   - Form and Tree (List) views for data entry.
   - Interactive status bar (Draft -> Process -> Done).
   - Dedicated root menu and submenus for Moci Petshop operations.

3. **Automated Sequence Generation**
   - Automatically generates unique, formatted Reference IDs for every new grooming service (e.g., `GRM/2026/0001`).

4. **Cross-Module Integration (Sales Order)**
   - Python-driven action button that automatically generates a Draft Sales Order (SO) in Odoo's native Sales module based on the grooming service data.
   - Automatically creates or links a "Layanan Petshop" service product in the database to fulfill Odoo's strict accounting rules.

## 🛠️ Tech Stack
* **Framework:** Odoo 16
* **Backend:** Python 3 (Odoo ORM)
* **Frontend:** XML (Odoo Views)
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker & Docker Compose (Linux containerized environment)

## 🚀 How to Run Locally

To test this module on your local machine using Docker:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Zahran2/odoo-moci-porto.git
   cd odoo-moci-porto
   ```

2. **Start the containers**
   Make sure you have Docker Desktop installed, then run:
   ```bash
   docker-compose up -d
   ```

3. **Install the Module in Odoo**
   - Open your browser and go to `http://localhost:8069`
   - Create a new database (e.g., `moci_erp`).
   - Activate **Developer Mode** (Settings -> Scroll down -> Activate the developer mode).
   - Go to the **Apps** menu.
   - Click **Update Apps List** in the top navigation bar and click Update on the pop-up.
   - Remove the `Apps` search filter, search for `Moci Petshop`, and click **Activate**.

## 📸 Screenshots
<img width="1365" height="322" alt="image" src="https://github.com/user-attachments/assets/636c4a87-e3ed-43a2-bcf2-b7624c254622" />
<img width="1365" height="273" alt="image" src="https://github.com/user-attachments/assets/dbb4b6be-c7f5-47d8-ab2c-5348d17ab8ce" />
<img width="1365" height="403" alt="image" src="https://github.com/user-attachments/assets/0043d7fc-25a5-4bb1-9f41-5dba216d4777" />


## 👨‍💻 About the Developer

**Zahran Anugerah Rizqullah**

I am a recent D4 Teknik Informatika graduate from Politeknik Negeri Bandung with full-stack development experience. Having previously built a standalone POS desktop application for my family's business (Moci Petshop), I adapted its business logic into this Odoo ERP module. I am a person who enjoys learning new technologies and continuously improving my problem-solving skills in software engineering.
