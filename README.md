# WordPress Multi-Page Website Setup

Welcome to your local WordPress development environment! Everything has been configured and prepared for you to build a multi-page website.

---

## 🚀 Quick Start (Running in 1 Click)

1. **Start the WordPress Server**:
   - Double-click `start-wordpress.bat` (or run `.\start-wordpress.ps1` in PowerShell).
   - This automatically launches the PHP server and opens your browser at **http://localhost:8080/**.

2. **Complete the 1-Minute WordPress Installer**:
   - Go to: **[http://localhost:8080/](http://localhost:8080/)** (or `http://localhost:8080/wp-admin/install.php`)
   - Fill in:
     - **Site Title**: (e.g., *My Business Website*)
     - **Username**: (e.g., *admin*)
     - **Password**: (choose your desired password)
     - **Email**: (your email address)
   - Click **Install WordPress** & Log In!

3. **Generate Starter Pages (Home, About, Services, Portfolio, Contact)**:
   - Once logged in, double-click `create-pages.bat`.
   - This script automatically publishes 5 core pages and assigns the "Home" page as your static front page!

---

## 🎨 Themes & Page Builders Included

- **Astra Theme** (`wp-content/themes/astra`): The fastest, most customizable WordPress theme designed specifically for multi-page websites and page builders.
- **Twenty Twenty-Five** (`wp-content/themes/twentytwentyfive`): WordPress's modern Full-Site Editing block theme.
- **Elementor** (`wp-content/plugins/elementor`): The visual drag-and-drop website and page builder. Simply activate it under **Plugins > Installed Plugins** to design custom layouts with ease.

---

## 🛠️ Included Tools & Scripts

| File | Purpose |
|---|---|
| `start-wordpress.bat` | 1-click startup script that starts the web server & opens browser |
| `start-wordpress.ps1` | PowerShell equivalent launcher |
| `create-pages.bat` | Automatically creates standard website pages (Home, About, Services, etc.) |
| `wp.bat` | WP-CLI wrapper (e.g. `wp plugin list`, `wp post list`) |
| `wp-config.php` | Pre-configured WordPress settings file |

---

## 🗄️ Database Options

1. **Default (Zero-Config SQLite)**:
   - Powered by the official WordPress Performance Team SQLite drop-in (`wp-content/db.php`).
   - Requires **no database passwords or server configuration** — works immediately!
   
2. **Switch to MySQL 8.0 (Optional)**:
   - Your computer already has MySQL 8.0 installed (`MySQL80` service).
   - To switch to MySQL:
     1. Delete or rename `wordpress/wp-content/db.php`.
     2. Create a database in MySQL (e.g., `CREATE DATABASE wordpress_db;`).
     3. Update `DB_NAME`, `DB_USER`, `DB_PASSWORD` in `wordpress/wp-config.php`.
