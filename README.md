# Library Management App

A custom Frappe app for managing library books and loans.

## Installation

### 1. Clone the Repository
```sh
cd ~/frappe-bench
bench get-app library_management https://github.com/chiz-kb/library_management.git
```
Once the app is downloaded, install it on your Frappe site:
### 2. Install the App

```sh
bench --site mysite install-app library_management
```
Replace mysite with your actual site name.
### 3. Restart Bench
After installation, restart your Frappe server:
```sh
bench restart
```
