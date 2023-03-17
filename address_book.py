from tkinter import *
import sqlite3

root = Tk()
root.title("Learn cody")
root.geometry("400x600")


# Create a table

# c.execute("""CREATE TABLE addresses (
#         first name text,
#         last name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")


# Create function for delete
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE FROM addresses_2 where oid=" + delete_entry.get())

    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_entry.get()

    c.execute(""" UPDATE addresses_2 SET 
            "first_name" = :first_name,
            "last_name" = :last_name,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode    

            WHERE oid = :oid
    """, {
        'first_name': first_name_edit.get(),
        'last_name': last_name_edit.get(),
        'address': address_edit.get(),
        'city': city_edit.get(),
        'state': state_edit.get(),
        'zipcode': zipcode_edit.get(),
        'oid': record_id
    })

    conn.commit()
    conn.close()

    editor.destroy()


# Create function for edit
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap('images/clock.ico')
    editor.geometry("400x200")

    # Create a database or open
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the databasa
    record_id = delete_entry.get()
    c.execute("SELECT * FROM addresses_2 WHERE oid = " + record_id)
    records = c.fetchall()

    # label_records = Label(root, text=print_records)
    # label_records.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    global first_name_edit
    global last_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    first_name_edit = Entry(editor, width=30)
    first_name_edit.grid(row=0, column=1, padx=20, pady=(10, 0))
    last_name_edit = Entry(editor, width=30)
    last_name_edit.grid(row=1, column=1)
    address_edit = Entry(editor, width=30)
    address_edit.grid(row=2, column=1)
    city_edit = Entry(editor, width=30)
    city_edit.grid(row=3, column=1)
    state_edit = Entry(editor, width=30)
    state_edit.grid(row=4, column=1)
    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row=5, column=1)

    # Create Text Box Labels
    first_name_label = Label(editor, text="First name")
    first_name_label.grid(row=0, column=0, pady=(10, 0))
    last_name_label = Label(editor, text="Last name")
    last_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop thru results
    for i in records:
        first_name_edit.insert(0, i[0])
        last_name_edit.insert(0, i[1])
        address_edit.insert(0, i[2])
        city_edit.insert(0, i[3])
        state_edit.insert(0, i[4])
        zipcode_edit.insert(0, i[5])

    save_button = Button(editor, text="Save Record", command=update)
    save_button.grid(row=6, column=0, padx=10, pady=10, ipadx=107, columnspan=3)


def submit():
    # Create a database or open
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses_2 values(:first_name, :last_name, :address, :city, :state, :zipcode)",
              {
                  'first_name': first_name.get(),
                  'last_name': last_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear The Text Boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query function
def query():
    # Create a database or open
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses_2")
    records = c.fetchall()
    # print(records)

    print_records = ""
    for i in records:
        print_records += str(i[0]) + " " + str(i[1]) + " " + "\t" + str(i[6]) + "\n"

    label_records = Label(root, text=print_records)
    label_records.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_entry = Entry(root, width=30)
delete_entry.grid(row=9, column=1, pady=(20, 0))

# Create Text Box Labels
first_name_label = Label(root, text="First name")
first_name_label.grid(row=0, column=0, pady=(10, 0))
last_name_label = Label(root, text="Last name")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_label = Label(root, text='Select ID')
delete_label.grid(row=9, column=0, pady=(20, 0))

# Create Submit Button
submit_button = Button(root, text='Submit', command=submit)
submit_button.grid(row=6, column=0, padx=10, pady=10, ipadx=100, columnspan=3)

query_button = Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, padx=10, pady=10, ipadx=100, columnspan=3)

delete_button = Button(root, text="Delect Record", command=delete)
delete_button.grid(row=10, column=0, padx=10, pady=10, ipadx=100, columnspan=3)

edit_button = Button(root, text="Edit Record", command=edit)
edit_button.grid(row=11, column=0, padx=10, pady=10, ipadx=107, columnspan=3)

root.mainloop()
