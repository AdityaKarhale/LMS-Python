📚 Library Management System – Mini Project
A simple desktop-based Library Management System developed using Python with a Tkinter GUI and SQLite database. The system helps manage library operations like issuing and returning books, adding students and books, and tracking history.

🛠 Technologies Used
Python (Core Language)

Tkinter (GUI Library)

SQLite3 (Local Database)

📂 Project Structure

library-management-system/
│
├── main.py       # Contains all backend logic (database operations, business logic)
├── gui.py        # All GUI windows using Tkinter
├── library_db.db # SQLite database file 
└── README.md     # Project documentation


🎯 Features
✅ Issue Book
✅ Return Book
✅ View Not Returned Books
✅ Search Student
✅ Search Book
✅ View Student History
✅ View Book History
✅ Add New Book
✅ Add New Student

🧠 How It Works
Database:

Uses SQLite tables: all_books, all_studs, and all_issued.

All DML operations (INSERT, UPDATE) and SELECT queries are managed in main.py.

GUI:

GUI is built using Tkinter (gui.py).

Each operation has its own popup window for clean input/output.

Input validation and user feedback via messagebox.

🚀 How to Run
Clone the repository:
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
Run the setup.py first
Run the gui.py 


