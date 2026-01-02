# 🛠️ Service Desk: Ticket Management System (TMS)

## 📌 Project Overview
The **Service Desk TMS** is an enterprise-grade incident management application designed to bridge the gap between software engineering and business operations. Inspired by **SAP Service Cloud** workflows, this system allows organizations to digitize their technical support lifecycle—from initial reporting to final resolution.

This project demonstrates a clear **Client-Server Architecture**, moving from a basic Python logic to a functional web-based API integrated with a persistent database.

---

## 🏗️ System Architecture
The application is built using a modern decoupled architecture:

* **Frontend (Client):** Developed using **HTML5** and **CSS3** for a professional, responsive user interface.
* **Backend (API):** A **Python (Flask)** API that handles business logic, priority processing, and server-side routing.
* **Database (Storage):** **SQL (SQLite)** serves as the "Source of Truth," ensuring all tickets are stored persistently.



---

## 🚀 Key Features
The system is built around three core enterprise functionalities:

1.  **Create Ticket:** * Users can log incidents with detailed descriptions.
    * Each entry is automatically timestamped for audit purposes.
2.  **Assign Priorities:** * Mimics SAP business logic by allowing users to categorize tickets as **High, Medium, or Low**.
    * High-priority tickets are visually flagged to ensure SLA (Service Level Agreement) compliance.
3.  **Resolve Ticket:** * Enables a full lifecycle loop by allowing administrators to close tickets once the issue is fixed.
    * Updates the database status in real-time.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Framework** | Flask (Lightweight API) |
| **UI/UX** | HTML5, CSS3 |
| **Database** | SQL (SQLite) |
| **Workflow** | SAP-Inspired Incident Management |

---

## 📊 Database Schema
The system uses a relational model to manage data integrity:



---
## 📥 Getting Started

### Prerequisites
* Python 3.x installed.
* Flask library installed (pip install flask).

### Installation & Execution
1.  *Clone the repository:*
    git clone https://github.com/SvaraShah/Servicedesk-Ticket-Management-System---web.git
2.  *Navigate to the directory and run the application:*
    cd Service-Desk-Web
    python servicedesk.py
    
3.  *Access the Dashboard:*
    Open your browser and visit: http://127.0.0.1:5000

---

## 👤 Author
*Svara Pankilkumar Shah*
B.Tech CSE with SAP Specialization | 2nd Year
Parul University
