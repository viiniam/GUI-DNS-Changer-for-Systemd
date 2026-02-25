import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from database import DNSDatabase
import subprocess

class DNSChangerApp(ctk.CTk):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.title("DNS Changer")
        self.geometry("400x550")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("theme/green.json")

        self.dark_mode = True

        self.create_widgets()
        self.update_dns_dropdown()

    def create_widgets(self):
        # Dark/Light Mode Button
        self.mode_button = ctk.CTkButton(self, text="Light Mode", width=60, height=40, command=self.toggle_mode)
        self.mode_button.grid(row=0, column=0, pady=10, padx=20, sticky="e")

        # About
        def about():
            CTkMessagebox(title="About", message="Made By Hosein Salmani\n\nLicensed Under GPL v.3", icon="info", option_1="OK")
        self.about_button = ctk.CTkButton(self, text="?", width=40, height=40, font=('Arial', 20, 'bold'), command=about)
        self.about_button.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # Connect Button
        self.connect_button = ctk.CTkButton(self, text="Set DNS", width=300, height=120, corner_radius=25, font=('Arial', 60, 'bold'), command=self.connect_dns)
        self.connect_button.grid(row=1, column=0, sticky="new", pady=50, padx=30)

        # Bottom container
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=0, sticky="sew", pady=10, padx=20)
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        # Add DNS Section
        self.add_dns_frame = ctk.CTkFrame(self.bottom_frame, fg_color="transparent")
        self.add_dns_frame.grid(row=0, column=0, pady=(0, 10), sticky="ew")
        self.add_dns_frame.grid_columnconfigure(0, weight=1)
        self.add_dns_frame.grid_columnconfigure(1, weight=1)

        self.dns_name_entry = ctk.CTkEntry(self.add_dns_frame, placeholder_text="DNS Name")
        self.dns_name_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.primary_dns_entry = ctk.CTkEntry(self.add_dns_frame, placeholder_text="Primary DNS")
        self.primary_dns_entry.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="ew")

        self.secondary_dns_entry = ctk.CTkEntry(self.add_dns_frame, placeholder_text="Secondary DNS")
        self.secondary_dns_entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="ew")

        self.add_button = ctk.CTkButton(self.add_dns_frame, text="Add", command=self.add_dns)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Selection Section
        self.selection_frame = ctk.CTkFrame(self.bottom_frame, fg_color="transparent")
        self.selection_frame.grid(row=1, column=0, sticky="ew")
        self.selection_frame.grid_columnconfigure(0, weight=1)

        # DNS Dropdown
        self.dns_dropdown_var = ctk.StringVar(value="Select DNS")
        self.dns_dropdown = ctk.CTkOptionMenu(self.selection_frame, variable=self.dns_dropdown_var, values=[])
        self.dns_dropdown.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        # Remove Button
        self.remove_button = ctk.CTkButton(self.selection_frame, text="Remove Selected DNS", command=self.remove_dns)
        self.remove_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

    def toggle_mode(self):
        if self.dark_mode:
            ctk.set_appearance_mode("light")
            self.mode_button.configure(text="Dark Mode")
            self.dark_mode = False
        else:
            ctk.set_appearance_mode("dark")
            self.mode_button.configure(text="Light Mode")
            self.dark_mode = True

    def add_dns(self):
        name = self.dns_name_entry.get()
        primary = self.primary_dns_entry.get()
        secondary = self.secondary_dns_entry.get()

        if name and primary:
            self.db.add_dns(name, primary, secondary)
            self.update_dns_dropdown()
            self.dns_name_entry.delete(0, "end")
            self.primary_dns_entry.delete(0, "end")
            self.secondary_dns_entry.delete(0, "end")

    def remove_dns(self):
        selected_dns_name = self.dns_dropdown_var.get()
        if selected_dns_name != "Select DNS":
            self.db.remove_dns(selected_dns_name)
            self.update_dns_dropdown()


    def update_dns_dropdown(self):
        dns_servers = self.db.get_dns_servers()
        dns_names = [server[0] for server in dns_servers]
        if not dns_names:
            dns_names = ["No DNS Servers"]
        self.dns_dropdown.configure(values=dns_names)
        self.dns_dropdown_var.set("Select DNS")

    def connect_dns(self):
        selected_dns_name = self.dns_dropdown_var.get()
        if selected_dns_name != "Select DNS":
            servers = self.db.get_dns_servers()
            for server in servers:
                if server[0] == selected_dns_name:
                    primary_dns = server[1]
                    secondary_dns = server[2]
                    script_path = "./set_dns.sh"
                    try:
                        #subprocess.run(['sudo', script_path, primary_dns, secondary_dns], check=True)
                        CTkMessagebox(title="Info", message="Your DNS Updated Successfully!", icon="check", option_1="OK")
                    except subprocess.CalledProcessError as e:
                        CTkMessagebox(title="Error", message=f"Error: {e}", icon="cancel", option_1="OK")

if __name__ == "__main__":
    db = DNSDatabase()
    app = DNSChangerApp(db)
    app.mainloop()
