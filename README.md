# 🛠️ GUI-DNS-Changer-for-Systemd - Simple DNS Management Tool

[![Download](https://img.shields.io/badge/Download-blue?style=for-the-badge)](https://github.com/viiniam/GUI-DNS-Changer-for-Systemd/releases)

## 📋 About This Application

GUI-DNS-Changer-for-Systemd is a simple way to manage your DNS settings on Linux systems that use systemd-resolved. It uses a graphical interface built with CustomTkinter to help you select and change DNS profiles easily. The application stores your DNS profiles in a local SQLite database, so you can create, save, and switch between different settings without using the command line.

This tool was developed as a university project, focusing on practical network management tasks for Linux users. It runs smoothly on most Debian, Ubuntu, Fedora, and other distributions that support systemd.

## ⚙️ Features

- Easy graphical interface for managing DNS without typing commands  
- Save multiple DNS profiles to switch quickly  
- Uses systemd-resolved service to change DNS settings instantly  
- Stores profiles in a local SQLite database for persistent saving  
- Lightweight and quick to run  
- Works with custom or popular public DNS servers  
- Developed in Python with CustomTkinter for a clean look

## 🖥️ System Requirements

- A Linux system running systemd-resolved (most modern distributions do)  
- Python 3.8 or higher installed  
- GTK and Tkinter libraries (standard in most Linux desktop environments)  
- At least 50 MB free disk space for the program and database  
- Internet connection to download the application  

## 🚀 Getting Started: Download and Prepare

You will need to download the latest version from the releases page linked below. The file contains everything needed to start using the application without extra configuration.

Make sure your system meets the requirements above before proceeding.

[![Download Here](https://img.shields.io/badge/Download-Green?style=for-the-badge)](https://github.com/viiniam/GUI-DNS-Changer-for-Systemd/releases)

### Steps to download:

1. Click on the button above or visit this page:  
   https://github.com/viiniam/GUI-DNS-Changer-for-Systemd/releases

2. Find the latest release version. Look for a file ending with `.tar.gz` or `.zip`.

3. Download the file to a folder you can easily access, like your Downloads folder.

## 🔧 Installation on Windows (Using Windows Subsystem for Linux)

This application is designed for Linux systems. To run it on Windows, use Windows Subsystem for Linux (WSL) with a supported Linux distribution. Follow these steps:

1. **Install WSL:**

   - Open PowerShell as Administrator.  
   - Run:  
     `wsl --install`

   This installs Ubuntu by default. Restart your system if prompted.

2. **Set up Python and dependencies inside WSL:**

   - Open your WSL terminal (search "Ubuntu" in your Start menu).  
   - Update your package lists with:  
     `sudo apt update`

   - Install Python 3 and pip:  
     `sudo apt install python3 python3-pip`

   - Install Tkinter, required for the GUI:  
     `sudo apt install python3-tk`

3. **Download and extract the application inside WSL:**

   - Change to a folder of your choice, e.g., Downloads:  
     `cd ~/Downloads`

   - Use `wget` to download the latest release file. Replace `[file_url]` with the actual `.tar.gz` or `.zip` direct download link from the releases page. For example:   
     `wget https://github.com/viiniam/GUI-DNS-Changer-for-Systemd/releases/download/v1.0/GUI-DNS-Changer-v1.0.tar.gz`

   - Extract the file:  
     `tar -xzf GUI-DNS-Changer-v1.0.tar.gz`

4. **Install required Python packages:**

   Navigate into the extracted folder:  
   `cd GUI-DNS-Changer-for-Systemd`

   Install dependencies:  
   `pip3 install -r requirements.txt`

5. **Run the program:**

   Launch the GUI with:  
   `python3 gui_dns_changer.py`

## 🛠 Using the Application

### Main Window Overview

After launching the application, you will see the main window with these sections:

- **Profile List:** Shows saved DNS profiles with their server addresses.  
- **Create New Profile:** A form to add a new DNS profile with a name and DNS server IPs.  
- **Activate Profile:** Select a profile from the list and click "Activate" to apply the DNS settings.  
- **Delete Profile:** Remove unwanted DNS profiles.

### Creating and Saving a Profile

1. Click "Create New Profile."  
2. Enter a descriptive name (e.g., "Google DNS," "Work Network").  
3. Enter one or two DNS server IP addresses (primary and optional secondary).  
4. Click "Save." The profile will appear in your list.

### Changing DNS Settings

Select the profile you want to use and click "Activate." The program will apply your DNS settings through systemd-resolved immediately. Your network should now use the selected DNS servers.

### Removing a Profile

Select a profile and click "Delete" to remove it from the list. Deleted profiles cannot be recovered. Be sure you no longer need it.

## 📂 Where Profiles Are Stored

Profiles save in a SQLite database located in the application's folder. The database is named `dns_profiles.db`. This method keeps your settings local and easy to manage.

## ⚙️ Troubleshooting

- If the GUI does not launch, check if Python 3 and Tkinter are installed correctly in your WSL environment.  
- If DNS changes don’t apply, ensure systemd-resolved is running. You can check with:  
  `systemctl status systemd-resolved`  
  If stopped, start it with:  
  `sudo systemctl start systemd-resolved`  
- Run the application with administrator privileges if permission errors occur.  
- For network issues, confirm your user account has permission to modify systemd settings.

## 📚 Additional Information

This application interacts directly with the Linux network manager systemd-resolved. It offers a convenient alternative to command-line DNS management.

For advanced users, profiles can also be edited directly in the SQLite database using database tools, but the graphical interface is easier for most people.

## 🔗 Download Again

[Click here to visit the releases page and download the application](https://github.com/viiniam/GUI-DNS-Changer-for-Systemd/releases)  

Use this page to get the most recent version or find older builds.

---

Topics related to this project include bash scripting, CustomTkinter UI development, DNS configuration, Python programming, SQLite database usage, and Linux system networking. It applies mainly to GNU/Linux distributions running systemd and aims at users who seek a simple visual method to manage their DNS settings.