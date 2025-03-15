import tkinter as tk #consulted chatgpt on what modules to use and suggested tkinter for making GUI apps
from tkinter import messagebox #helps displays dialogue boxes for alerts and stuff

class MotorcycleAccidentDetector:
    def __init__(self, root): #function to setup main window, this runs first when program starts
        self.root = root
        self.root.title("Motorcycle Accident Detector - Accidento") #sets the title at top of window
        self.root.geometry("800x600") #makes window 800 pixels wide and 600 pixels tall
        self.root.resizable(False, False) #stops user from resizing window which might mess up layout
        self.create_frames() #calls other functions to build the app
        self.setup_emergency_contacts()
        self.setup_speedometer()
        self.setup_simulation_controls()

    def create_frames(self): #function to divide the main window into two sections side by side
        self.contacts_frame = tk.Frame(self.root, width=300, height=600, bg="#f0f0f0", bd=1, relief=tk.SOLID) #emergency contact management section on left side
        self.contacts_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10) #padding of 10 pixels around the edges
        
        self.control_frame = tk.Frame(self.root, width=500, height=600, bd=1, relief=tk.SOLID) #speedometer and simulation controls on right side
        self.control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10) #expand=True makes it fill available space

    def setup_emergency_contacts(self):#function for left panel interface with contacts list
        title_label = tk.Label( #label at the top saying "Emergency Contacts"
            self.contacts_frame,
            text="Emergency Contacts",
            font=("Arial", 16, "bold"), #makes text bigger and bold
            bg="#f0f0f0" #background color matching the frame
        )
        title_label.pack(pady=10)
        list_frame = tk.Frame(self.contacts_frame, bg="#f0f0f0")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.contacts_listbox = tk.Listbox(list_frame, width=30, height=15) #this shows the list of contacts
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame) #scroll bar for when we have lots of contacts
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.contacts_listbox.config(yscrollcommand=scrollbar.set) #connects listbox to scrollbar
        scrollbar.config(command=self.contacts_listbox.yview) #connects scrollbar to listbox
        
        example_contacts = [ #example contacts to show in the list when program starts
            "Emergency Services (911)",
            "John Doe (Family)",
            "Jane Smith (Friend)"
        ]
        for contact in example_contacts: #adds each contact from the list above
            self.contacts_listbox.insert(tk.END, contact)
        
        buttons_frame = tk.Frame(self.contacts_frame, bg="#f0f0f0")
        buttons_frame.pack(fill=tk.X, pady=10)
        
        add_btn = tk.Button(buttons_frame, text="Add Contact", command=self.placeholder) #button doesn't do anything yet
        add_btn.grid(row=0, column=0, padx=5, pady=5) #using grid to organize buttons in rows and columns
        edit_btn = tk.Button(buttons_frame, text="Edit Contact", command=self.placeholder) #contact management buttons for editing existing contacts
        edit_btn.grid(row=0, column=1, padx=5, pady=5)
        delete_btn = tk.Button(buttons_frame, text="Delete Contact", command=self.placeholder) #will delete selected contact later
        delete_btn.grid(row=1, column=0, padx=5, pady=5)
        view_btn = tk.Button(buttons_frame, text="View Details", command=self.placeholder) #will show more info about contact
        view_btn.grid(row=1, column=1, padx=5, pady=5)

    def setup_speedometer(self): #speedometer section on the right side
        title_label = tk.Label(
            self.control_frame,
            text="Speedometer",
            font=("Arial", 16, "bold") #big bold text for the title
        )
        title_label.pack(pady=10)
        
        self.speed_display = tk.Label( #display showing current speed with big font
            self.control_frame,
            text="0 km/h", #starts at zero
            font=("Arial", 40) #really big font so it's easy to read
        )
        self.speed_display.pack(pady=20)
        
        self.warning_label = tk.Label( #warning sign shows up when speed is dangerous
            self.control_frame,
            text="",
            font=("Arial", 12),
            fg="red" #red text for warning
        )
        self.warning_label.pack(pady=5)
        
        speed_controls = tk.Frame(self.control_frame)
        speed_controls.pack(pady=10)
        
        decrease_btn = tk.Button(speed_controls, text="Decrease Speed (S)", command=self.placeholder) #buttons for speed, S key will be shortcut
        decrease_btn.grid(row=0, column=0, padx=10)
        increase_btn = tk.Button(speed_controls, text="Increase Speed (W)", command=self.placeholder) #W key will increase speed like in games
        increase_btn.grid(row=0, column=1, padx=10)
        
        info_label = tk.Label( #labels and variables showing when warnings happen
            self.control_frame,
            text="Speed Thresholds:\n" + #\n means new line
                "Warning: >120 km/h\n" + #warning at 120
                "Critical: >200 km/h\n" + #critical warning at 200
                "Sudden Stop: ≥40 km/h decrease", #accident detection if speed drops by 40
            justify=tk.LEFT
        )
        info_label.pack(pady=10, anchor=tk.W)
    
    def setup_simulation_controls(self): #main control buttons at bottom of right panel
        controls_frame = tk.Frame(self.control_frame)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        
        start_btn = tk.Button( #button to start simulation with green color
            controls_frame,
            text="Start Simulation",
            command=self.placeholder,
            bg="#4CAF50", #green background
            fg="white", #white text
            width=15,
            height=2 #makes button bigger
        )
        start_btn.grid(row=0, column=0, padx=10, pady=10)
        
        end_btn = tk.Button( #end simulation button with red color
            controls_frame, 
            text="End Simulation",
            command=self.placeholder,
            bg="#F44336", #red background
            fg="white", #white text
            width=15,
            height=2
        )
        end_btn.grid(row=0, column=1, padx=10, pady=10)
        
        exit_btn = tk.Button( # program exit button with blue color
            controls_frame,
            text="Exit Program",
            command=self.exit_program, #this one actually works!
            bg="#2196F3", #blue background
            fg="white", #white text
            width=15,
            height=2
        ) 
        exit_btn.grid(row=0, column=2, padx=10, pady=10) #help
        
        help_btn = tk.Button( #help button in top left corner
            self.root,
            text="Help",
            command=self.show_help #shows instructions popup
        )
        help_btn.place(x=10, y=10) #placed at specific coordinates instead of grid
    
    def placeholder(self):
        messagebox.showinfo("Under Construction", "This feature will be implemented in the next phase.") #place holder message for unfinished buttons
    
    def show_help(self): #help text box function shows instructions
        help_text = """
MOTORCYCLE ACCIDENT DETECTOR HELP

This application will simulate a motorcycle accident detection system.

Features to be implemented:
- Emergency contact management
- Speed simulation and monitoring
- Accident detection
- Emergency notification system

This is just the GUI prototype. Full functionality will be added in the next phase.
"""
        messagebox.showinfo("Help", help_text) #creates popup with the help text
    def exit_program(self): #prompt to exit program with confirmation so you don't exit by accident
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"): #yes/no dialog
            self.root.destroy() #closes the window if user clicks OK

if __name__ == "__main__": #this is where the program starts running
    root = tk.Tk() #creates the main window
    app = MotorcycleAccidentDetector(root) #creates our application
    root.mainloop() #starts the program running
