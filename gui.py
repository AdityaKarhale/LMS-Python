import tkinter as tk
from tkinter import messagebox

import main

def issue_book_window():
    win = tk.Toplevel()
    win.title("Issue Book")
    win.geometry("450x700")
    win.resizable(False, False)

    # Labels
    l1 = tk.Label(win, text="Book Number:", font=("Arial", 12))
    l1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    l2 = tk.Label(win, text="Student Enrollment No:", font=("Arial", 12))
    l2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    # Entry Fields
    book_entry = tk.Entry(win, font=("Arial", 12))
    book_entry.grid(row=0, column=1, padx=10, pady=10)

    student_entry = tk.Entry(win, font=("Arial", 12))
    student_entry.grid(row=1, column=1, padx=10, pady=10)

    # Submit Button Callback
    def on_submit():
        book_num = book_entry.get().strip()
        student_enroll = student_entry.get().strip()

        # Validation
        if not book_num or not student_enroll:
            messagebox.showwarning("Input Error", "Both fields are required.")
            return
        if not book_num.isdigit() or not student_enroll.isdigit():
            messagebox.showerror("Validation Error", "Book number and enrollment number must be numeric.")
            return

        # Issue Book Logic
        result = main.issue_book(book_num, student_enroll)
        messagebox.showinfo("Success", result)
        win.destroy()

    # Submit Button
    submit_btn = tk.Button(win, text="Issue Book", font=("Arial", 12), command=on_submit)
    submit_btn.grid(row=2, column=0, columnspan=2, pady=20)


def return_book_window():
    win = tk.Toplevel()
    win.title("Return Book")
    win.geometry("450x700")
    win.resizable(False, False)

    # Labels
    l1 = tk.Label(win, text="Book Number:", font=("Arial", 12))
    l1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    # Entry Fields
    book_entry = tk.Entry(win, font=("Arial", 12))
    book_entry.grid(row=0, column=1, padx=10, pady=10)

    # Submit Button Callback
    def on_submit():
        book_num = book_entry.get().strip()

        # Validation
        if not book_num:
            messagebox.showwarning("Input Error", "Book number is required.")
            return
        if not book_num.isdigit():
            messagebox.showerror("Validation Error", "Book number must be numeric.")
            return

        # Return Book Logic
        result = main.return_book(book_num)
        messagebox.showinfo("Success", result)
        win.destroy()

    # Submit Button
    submit_btn = tk.Button(win, text="Return Book", font=("Arial", 12), command=on_submit)
    submit_btn.grid(row=1, column=0, columnspan=2, pady=20)


def view_not_returned_window():
    win = tk.Toplevel()
    win.title("Not Returned Books")
    win.geometry("500x400")
    win.resizable(False, False)

    # Heading Label
    tk.Label(win, text="Books Not Yet Returned", font=("Arial", 14, "bold")).pack(pady=10)

    # Frame for list content
    frame = tk.Frame(win)
    frame.pack(pady=10)

    # Column headers
    header = tk.Label(frame, text="Enrollment\tBook No\tIssue Date", font=("Arial", 12, "underline"), justify="left")
    header.pack(anchor="w")

    # Fetch and display data
    data = main.view_not_ret()
    if not data:
        tk.Label(frame, text="No books pending return.", font=("Arial", 12), fg="red").pack(anchor="w", pady=10)
    else:
        for rec in data:
            line = f"{rec[0]}\t\t{rec[1]}\t\t{rec[2]}"
            tk.Label(frame, text=line, font=("Arial", 12), justify="left").pack(anchor="w")

    # Close button
    tk.Button(win, text="Close", font=("Arial", 11), command=win.destroy).pack(pady=10)




def search_student_window():
    win = tk.Toplevel()
    win.title("Search Student")
    win.geometry("400x300")
    win.resizable(False, False)

    # Label and Entry
    tk.Label(win, text="Enter Enrollment Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=15, sticky="e")
    enroll_entry = tk.Entry(win, font=("Arial", 12))
    enroll_entry.grid(row=0, column=1, padx=10, pady=15)

    result_frame = tk.Frame(win)
    result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def on_search():
        senroll = enroll_entry.get().strip()

        if not senroll:
            messagebox.showwarning("Input Error", "Enrollment number is required.")
            return
        if not senroll.isdigit():
            messagebox.showerror("Validation Error", "Enrollment number must be numeric.")
            return

        for widget in result_frame.winfo_children():
            widget.destroy()

        result = main.search_stud(senroll)
        if not result:
            tk.Label(result_frame, text="Invalid Enrollment Number", font=("Arial", 12), fg="red").pack()
        else:
            name, email, mobile = result[0]
            tk.Label(result_frame, text=f"Name: {name}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(result_frame, text=f"Email: {email}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(result_frame, text=f"Mobile: {mobile}", font=("Arial", 12)).pack(anchor="w")

    # Search Button
    search_btn = tk.Button(win, text="Search", font=("Arial", 12), command=on_search)
    search_btn.grid(row=1, column=0, columnspan=2, pady=10)


def search_book_window():
    win = tk.Toplevel()
    win.title("Search Book")
    win.geometry("400x300")
    win.resizable(False, False)

    # Book number input
    tk.Label(win, text="Enter Book Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=15, sticky="e")
    book_entry = tk.Entry(win, font=("Arial", 12))
    book_entry.grid(row=0, column=1, padx=10, pady=15)

    result_frame = tk.Frame(win)
    result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def on_search():
        bnum = book_entry.get().strip()

        if not bnum:
            messagebox.showwarning("Input Error", "Book number is required.")
            return
        if not bnum.isdigit():
            messagebox.showerror("Validation Error", "Book number must be numeric.")
            return

        for widget in result_frame.winfo_children():
            widget.destroy()

        result = main.search_book(bnum)
        if not result:
            tk.Label(result_frame, text="Invalid Book Number", font=("Arial", 12), fg="red").pack()
        else:
            title, author, pub = result[0]
            tk.Label(result_frame, text=f"Title: {title}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(result_frame, text=f"Author: {author}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(result_frame, text=f"Publisher: {pub}", font=("Arial", 12)).pack(anchor="w")

    # Search button
    tk.Button(win, text="Search", font=("Arial", 12), command=on_search).grid(row=1, column=0, columnspan=2, pady=10)



def student_history_window():
    win = tk.Toplevel()
    win.title("Student History")
    win.geometry("500x400")
    win.resizable(False, False)

    # Enrollment input
    tk.Label(win, text="Enter Enrollment Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=15, sticky="e")
    enroll_entry = tk.Entry(win, font=("Arial", 12))
    enroll_entry.grid(row=0, column=1, padx=10, pady=15)

    result_frame = tk.Frame(win)
    result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def on_search():
        senr = enroll_entry.get().strip()

        if not senr:
            messagebox.showwarning("Input Error", "Enrollment number is required.")
            return
        if not senr.isdigit():
            messagebox.showerror("Validation Error", "Enrollment number must be numeric.")
            return

        for widget in result_frame.winfo_children():
            widget.destroy()

        data = main.stud_history(senr)
        if not data:
            tk.Label(result_frame, text="No Record found.", font=("Arial", 12), fg="red").pack()
        else:
            output = tk.Text(result_frame, font=("Courier New", 12), height=15, width=60)
            output.pack()

            output.insert(tk.END, f"{'Book No':<10}{'Issue Date':<15}{'Return Date':<15}{'Returned':<10}\n")
            output.insert(tk.END, "-" * 55 + "\n")

            for rec in data:
                rdate = rec[2] if rec[2] else '-'
                line = f"{rec[0]:<10}{rec[1]:<15}{rdate:<15}{rec[3]:<10}\n"
                output.insert(tk.END, line)

            output.config(state="disabled")
    # Search button
    tk.Button(win, text="Search", font=("Arial", 12), command=on_search).grid(row=1, column=0, columnspan=2, pady=10)


import tkinter as tk
from tkinter import messagebox
from main import book_history

def book_history_window():
    win = tk.Toplevel()
    win.title("Book History")
    win.geometry("500x400")
    win.resizable(False, False)

    # Book number input
    tk.Label(win, text="Enter Book Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=15, sticky="e")
    book_entry = tk.Entry(win, font=("Arial", 12))
    book_entry.grid(row=0, column=1, padx=10, pady=15)

    result_frame = tk.Frame(win)
    result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def on_search():
        bnum = book_entry.get().strip()

        if not bnum:
            messagebox.showwarning("Input Error", "Book number is required.")
            return
        if not bnum.isdigit():
            messagebox.showerror("Validation Error", "Book number must be numeric.")
            return

        for widget in result_frame.winfo_children():
            widget.destroy()

        data = book_history(bnum)
        if not data:
            tk.Label(result_frame, text="No Record found.", font=("Arial", 12), fg="red").pack()
        else:
            output = tk.Text(result_frame, font=("Courier New", 12), height=15, width=60)
            output.pack()

            output.insert(tk.END, f"{'Enroll':<10}{'Issue Date':<15}{'Return Date':<15}{'Returned':<10}\n")
            output.insert(tk.END, "-" * 55 + "\n")

            for rec in data:
                rdate = rec[2] if rec[2] else '-'
                line = f"{rec[0]:<10}{rec[1]:<15}{rdate:<15}{rec[3]:<10}\n"
                output.insert(tk.END, line)

            output.config(state="disabled")

    # Search button
    tk.Button(win, text="Search", font=("Arial", 12), command=on_search).grid(row=1, column=0, columnspan=2, pady=10)

import tkinter as tk
from tkinter import messagebox
from main import add_new_book

def add_book_window():
    win = tk.Toplevel()
    win.title("Add New Book")
    win.geometry("400x300")
    win.resizable(False, False)

    # Labels and Entry widgets
    tk.Label(win, text="Book Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    bknum_entry = tk.Entry(win, font=("Arial", 12))
    bknum_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(win, text="Title:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    title_entry = tk.Entry(win, font=("Arial", 12))
    title_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(win, text="Author:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    author_entry = tk.Entry(win, font=("Arial", 12))
    author_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(win, text="Publication:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    pub_entry = tk.Entry(win, font=("Arial", 12))
    pub_entry.grid(row=3, column=1, padx=10, pady=10)

    def on_add():
        bknum = bknum_entry.get().strip()
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        publication = pub_entry.get().strip()

        if not (bknum and title and author and publication):
            messagebox.showwarning("Input Error", "All fields are required.")
            return
        if not bknum.isdigit():
            messagebox.showerror("Validation Error", "Book number must be numeric.")
            return

        try:
            add_new_book(bknum, title, author, publication)
            messagebox.showinfo("Success", "New Book Added.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add book.\n{e}")

    # Button to add book
    tk.Button(win, text="Add Book", font=("Arial", 12), command=on_add).grid(row=4, column=0, columnspan=2, pady=20)


import tkinter as tk
from tkinter import messagebox
from main import add_new_stud

def add_student_window():
    win = tk.Toplevel()
    win.title("Add New Student")
    win.geometry("400x320")
    win.resizable(False, False)

    # Labels and entries
    tk.Label(win, text="Enrollment Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    enr_entry = tk.Entry(win, font=("Arial", 12))
    enr_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(win, text="Name:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    name_entry = tk.Entry(win, font=("Arial", 12))
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(win, text="Mobile Number:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    mob_entry = tk.Entry(win, font=("Arial", 12))
    mob_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(win, text="Email Address:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(win, font=("Arial", 12))
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    def on_add():
        senroll = enr_entry.get().strip()
        name = name_entry.get().strip()
        mob = mob_entry.get().strip()
        email = email_entry.get().strip()

        if not (senroll and name and mob and email):
            messagebox.showwarning("Input Error", "All fields are required.")
            return
        if not senroll.isdigit() or not mob.isdigit():
            messagebox.showerror("Validation Error", "Enrollment and Mobile Number must be numeric.")
            return

        try:
            add_new_stud(senroll, name, mob, email)
            messagebox.showinfo("Success", "New Student Added.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add student.\n{e}")

    # Button
    tk.Button(win, text="Add Student", font=("Arial", 12), command=on_add).grid(row=4, column=0, columnspan=2, pady=20)

# GUI setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("450x700")
root.resizable(False, False)

# === Title ===
title_label = tk.Label(root, text="Library Management System", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# === Frame for Buttons ===
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# === Buttons ===
btn1 = tk.Button(btn_frame, text="Issue Book", font=("Arial", 12), width=30, height=2, command=issue_book_window)
btn1.grid(row=0, column=0, padx=10, pady=5)

btn2 = tk.Button(btn_frame, text="Return Book", font=("Arial", 12), width=30, height=2, command=return_book_window)
btn2.grid(row=1, column=0, padx=10, pady=5)

btn3 = tk.Button(btn_frame, text="View Not Returned Books", font=("Arial", 12), width=30, height=2, command=view_not_returned_window)
btn3.grid(row=2, column=0, padx=10, pady=5)

btn4 = tk.Button(btn_frame, text="Search Student", font=("Arial", 12), width=30, height=2, command=search_student_window)
btn4.grid(row=3, column=0, padx=10, pady=5)

btn5 = tk.Button(btn_frame, text="Search Book", font=("Arial", 12), width=30, height=2, command=search_book_window)
btn5.grid(row=4, column=0, padx=10, pady=5)

btn6 = tk.Button(btn_frame, text="Student History", font=("Arial", 12), width=30, height=2, command=student_history_window)
btn6.grid(row=5, column=0, padx=10, pady=5)

btn7 = tk.Button(btn_frame, text="Book History", font=("Arial", 12), width=30, height=2, command=book_history_window)
btn7.grid(row=6, column=0, padx=10, pady=5)

btn8 = tk.Button(btn_frame, text="Add New Book", font=("Arial", 12), width=30, height=2, command=add_book_window)
btn8.grid(row=7, column=0, padx=10, pady=5)

btn9 = tk.Button(btn_frame, text="Add New Student", font=("Arial", 12), width=30, height=2, command=add_student_window)
btn9.grid(row=8, column=0, padx=10, pady=5)

btn0 = tk.Button(btn_frame, text="Exit", font=("Arial", 12), width=30, height=2, command=root.quit)
btn0.grid(row=9, column=0, padx=10, pady=5)

# === Run GUI ===
root.mainloop()

