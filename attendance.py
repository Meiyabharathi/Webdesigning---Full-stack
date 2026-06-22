import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- DATABASE ----------

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    date TEXT,
    status TEXT
)
""")

conn.commit()


# ---------- FUNCTIONS ----------

def add_record():

    name = name_entry.get()

    dept = dept_entry.get()

    date = date_entry.get()

    status = status_var.get()

    if name == "" or dept == "" or date == "":

        messagebox.showerror("Error", "Fill all fields")

        return

    cursor.execute(
        """
        INSERT INTO attendance(name,department,date,status)
        VALUES(?,?,?,?)
        """,
        (name, dept, date, status)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Attendance Added Successfully"
    )

    clear_fields()

    view_records()


def view_records():

    for item in tree.get_children():

        tree.delete(item)

    cursor.execute("SELECT * FROM attendance")

    rows = cursor.fetchall()

    for row in rows:

        tree.insert("", tk.END, values=row)


def search_record():

    date = date_entry.get()

    for item in tree.get_children():

        tree.delete(item)

    cursor.execute(
        """
        SELECT * FROM attendance
        WHERE date=?
        """,
        (date,)
    )

    rows = cursor.fetchall()

    for row in rows:

        tree.insert("", tk.END, values=row)


def delete_record():

    selected = tree.focus()

    if not selected:

        messagebox.showerror(
            "Error",
            "Select a record"
        )

        return

    values = tree.item(selected, "values")

    student_id = values[0]

    cursor.execute(
        "DELETE FROM attendance WHERE id=?",
        (student_id,)
    )

    conn.commit()

    view_records()

    messagebox.showinfo(
        "Success",
        "Deleted Successfully"
    )


def clear_fields():

    name_entry.delete(0, tk.END)

    dept_entry.delete(0, tk.END)

    date_entry.delete(0, tk.END)

    status_var.set("Present")


# ---------- GUI ----------

root = tk.Tk()

root.title("Attendance Management System")

root.geometry("900x600")


# Labels

tk.Label(root, text="Name").pack()

name_entry = tk.Entry(root, width=40)

name_entry.pack()


tk.Label(root, text="Department").pack()

dept_entry = tk.Entry(root, width=40)

dept_entry.pack()


tk.Label(root, text="Date (DD-MM-YYYY)").pack()

date_entry = tk.Entry(root, width=40)

date_entry.pack()


tk.Label(root, text="Status").pack()

status_var = tk.StringVar()

status_var.set("Present")

status_menu = tk.OptionMenu(
    root,
    status_var,
    "Present",
    "Absent"
)

status_menu.pack()


# Buttons

tk.Button(
    root,
    text="Add Attendance",
    command=add_record
).pack(pady=5)


tk.Button(
    root,
    text="Search By Date",
    command=search_record
).pack(pady=5)


tk.Button(
    root,
    text="View All",
    command=view_records
).pack(pady=5)


tk.Button(
    root,
    text="Delete",
    command=delete_record
).pack(pady=5)


# Table

columns = (
    "ID",
    "Name",
    "Department",
    "Date",
    "Status"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:

    tree.heading(col, text=col)

tree.pack(
    fill="both",
    expand=True,
    pady=20
)


view_records()

root.mainloop()

conn.close()
