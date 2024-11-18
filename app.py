import tkinter as tk
from tkinter import ttk
import datetime
import csv
from tkinter import messagebox
import pyttsx3
import dateutil.parser
from PIL import Image,ImageTk


text = pyttsx3.init()

def speak_text(command):
    text.say(command)
    text.runAndWait()

#font settings
font_o = ("Times New Roman" , 12) 
color = "blue"
background = 'white'
# Constants
MEDICATION_FILE = 'medication.csv'

# Function to load medication data from CSV
def load_medication_data():
    medication_data = []
    with open(MEDICATION_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            medication_data.append(row)
    return medication_data

# Function to display medication information
def display_medication_info():
    
    medication_data = load_medication_data()
    for row in medication_data:
        label_medication_name = tk.Label(top, text=row, font=font_o, fg=color, bg=background)
        label_medication_name.pack(pady=10)

# Function to set reminders for medication
def set_medication_reminders():
    medication_data = load_medication_data()
    current_time = datetime.datetime.now().strftime("%H:%M")

    for row in medication_data:
        medication_name = row[0]
        frequency = row[2]
        schedule_time_str = row[3]

        # Parse the schedule time string to a datetime object
        schedule_time = dateutil.parser.parse(schedule_time_str).strftime("%H:%M")

        if current_time == schedule_time:
            messagebox.showinfo("Medication Reminder", f"It's time to take {medication_name}.")
            print(f"Reminder: Take {medication_name}!")

# Function to add medication to the schedule
def add_medication_schedule():
    medication_name = entry_medication_name.get()
    dosage = entry_dosage.get()
    frequency = entry_frequency.get()
    schedule_time = entry_schedule_time.get()

    # Append the medication schedule to the CSV file
    with open(MEDICATION_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([medication_name, dosage, frequency, schedule_time])
    messagebox.showinfo("Success", "Medication schedule added successfully.")

def add_medication():
    top1 = tk.Toplevel()
    top1.title("Add Medication")
    top1.geometry("400x300")
    top1.config(bg=background)
    global entry_medication_name
    global entry_dosage
    global entry_frequency
    global entry_schedule_time

    # Medication Schedule Form
    label_medication_name = tk.Label(top1, text="Medication Name:", font=font_o, fg=color, bg=background)
    label_medication_name.pack(pady=5)
    entry_medication_name = tk.Entry(top1, font=font_o)
    entry_medication_name.pack(pady=5)

    label_dosage = tk.Label(top1, text="Dosage:", font=font_o, fg=color, bg=background)
    label_dosage.pack(pady=5)
    entry_dosage = tk.Entry(top1, font=font_o)
    entry_dosage.pack(pady=5)

    label_frequency = tk.Label(top1, text="Frequency:", font=font_o, fg=color, bg=background)
    label_frequency.pack(pady=5)
    entry_frequency = tk.Entry(top1, font=font_o)
    entry_frequency.pack(pady=5)

    label_schedule_time = tk.Label(top1, text="Schedule Time:", font=font_o, fg=color, bg=background)
    label_schedule_time.pack(pady=5)
    entry_schedule_time = tk.Entry(top1, font=font_o)
    entry_schedule_time.pack(pady=5)

    button_add_medication = tk.Button(top1, text="Add Medication", command=add_medication_schedule, font=font_o, fg="#000000", bg=background)
    button_add_medication.pack(pady=5)
    top1.after(500, speak_text, "You have clicked on Add Medication App. Kindly enter your Medication, Dosage, Frequency, and schedule time")
    top1.mainloop()

def display_medication():
    top = tk.Toplevel()
    top.title("Display Medication Reminder")
    top.geometry("600x400")
    top.config(bg=background)

    # Medication Schedule Form
    label_medication_name = tk.Label(top, text='Display Medication', font=font_o, fg=color, bg=background)
    label_medication_name.pack(pady=10)

    label_medication_info_btn = tk.Button(top, text='Click to view Medication', command=display_medication_info, font=font_o, fg="#000000", bg=background)
    label_medication_info_btn.pack(pady=10)

    top.after(500, speak_text, "You have clicked on Display Medication App successfully")
    top.mainloop()

def close():
    window.destroy()



def show_welcome_screen():
    # Clear window before showing name input screen
    for widget in window.winfo_children():
        widget.destroy()

    # Name entry form
    label_name_prompt = tk.Label(window, text="Please enter your full name:", font=font_o, fg=color, bg=background)
    label_name_prompt.pack(pady=20)

    entry_name = tk.Entry(window, font=font_o)
    entry_name.pack(pady=10)

    def submit_name():
        full_name = entry_name.get()
        if full_name:  # Check if name is entered
            window.after(500, welcome_user, full_name)  # Welcome after a slight delay
        else:
            messagebox.showwarning("Input Error", "Please enter a valid name")

    button_submit = tk.Button(window, text="Submit", command=submit_name, font=font_o, fg="#000000", bg=background)
    button_submit.pack(pady=10)

def welcome_user(full_name):
    # Clear window before displaying the app
    for widget in window.winfo_children():
        widget.destroy()

    # Welcome message
    label_welcome = tk.Label(window, text=f"Welcome, {full_name}!", font=("Arial", 16), bg=background, fg=color)
    label_welcome.pack(pady=20)

# Main window setup
    window.geometry("400x300")



#add image

    image_path = r'C:/Users/natha/OneDrive/Documents/GitHub/Medication-Reminder/medical_logo.png'

    try:
    # Open the image using Pillow (Image.open handles many formats)
        loaded_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(loaded_image)

    # Create a label to display the image
        image_label = tk.Label(window, image=tk_image)
        image_label.pack(side=tk.BOTTOM,pady=10)

    except Exception as e:
        print('error loading image:',e)

    # Create a label with custom styling
    label = tk.Label(window, text="Medication Reminder App", font=("Times New Roman", 20), pady=20, bg=background, fg=color)
    label.pack()

    # Create a styled frame for buttons
    button_frame = ttk.Frame(window, padding=20)
    button_frame.pack()

    # Create three styled buttons vertically aligned
    button1 = ttk.Button(button_frame, text="Add Medication", command=add_medication, style="Custom.TButton")
    button1.pack(pady=10)

    button2 = ttk.Button(button_frame, text="Display Medication", command=display_medication, style="Custom.TButton")
    button2.pack(pady=10)

    button3 = ttk.Button(button_frame, text="Set Reminder", command=set_medication_reminders, style="Custom.TButton")
    button3.pack(pady=10)

    button4 = ttk.Button(button_frame, text="Exit/Close", command=window.destory, style="Custom.TButton")
    button4.pack(pady=10)

    # Define custom styling for the buttons
    style = ttk.Style()
    style.configure("Custom.TButton", font=font_o, foreground=color, background=background, relief="raised")
    style.map("Custom.TButton", foreground=[('active', 'red'), ('disabled', 'gray')], background=[('active', '#0E4C3C'), ('disabled', 'gray')])

    window.after(500, speak_text, "Welcome to our advanced Medication Reminder App. It offers features to add, display, set reminders, and exit with ease.")


# Create the main window
window = tk.Tk()
window.title("Medication App")
window.config(bg=background)

# Request user name before proceeding to the app
show_welcome_screen()
# Start the main event loop
window.mainloop()
