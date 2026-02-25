# 🔧🐧 GUI-DNS-Changer-for-Systemd

A lightweight GUI application for managing DNS settings on **systemd-based GNU/Linux distributions**. Built with Python and CustomTkinter for an intuitive dark/light mode interface.

## ✨ Features

- 🌓 **Dark/Light Mode** - Toggle between themes
- 💾 **DNS Profiles** - Save and manage multiple DNS configurations
- ⚡ **Quick Apply** - One-click DNS switching via systemd-resolved
- 🎨 **Modern UI** - Clean CustomTkinter interface with green theme
- 📦 **Lightweight** - Minimal dependencies, fast and responsive

## 🎓 University Project

This is a simple university project created to demonstrate DNS management integration with systemd on GNU/Linux systems.

## 📋 Requirements

- **Python:** 3.10.12 or higher
- **OS:** GNU/Linux distributions using systemd

### Python Dependencies

```
customtkinter
CTkMessagebox
```

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cyberllloner/GUI-DNS-Changer-for-Systemd.git
   cd GUI-DNS-Changer-for-Systemd
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install customtkinter CTkMessagebox
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## 💡 How It Works

1. **Add DNS Profiles:** Enter a name and primary/secondary DNS addresses
2. **Select Profile:** Choose from saved DNS configurations
3. **Apply Settings:** Click "Set DNS" to apply via systemd-resolved
4. **Manage:** Remove unwanted DNS profiles anytime

The application modifies `/etc/systemd/resolved.conf` and restarts `systemd-resolved.service` to apply changes.

## 📂 Project Structure

```
.
├── main.py              # GUI application (CustomTkinter)
├── database.py          # SQLite database management
├── set_dns.sh          # Bash script for systemd-resolved integration
├── theme/
│   └── green.json      # Custom green theme
├── LICENSE             # GPL v3.0
└── README.md
```

## ⚠️ Important Notes

- Requires **root/sudo privileges** to modify DNS settings
- Works exclusively with **systemd-resolved** systems
- Database file (`dns_servers.db`) is created automatically on first run

## 📜 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

---

**Note:** This is an educational project shared as-is without ongoing maintenance or updates.
