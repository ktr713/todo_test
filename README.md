# Todo Desktop App

This project implements a simple ToDo application using a Flask backend and an Electron frontend for Windows.

## Contents

- **base.py**: The Flask backend server handling the ToDo application functionality.
- **requirements.txt**: Python dependencies for the Flask backend.
- **package.json**: Node project configuration for Electron.
- **main.js**: Electron main process file which spawns the Flask backend and creates the desktop window.

## Dependency Packages

### Python Dependencies

- Flask
- flask-cors

These are listed in the `requirements.txt` file.

### Node Dependencies

- Electron (version ^23.0.0)

These are listed in the `package.json` under `devDependencies`.

## Installation

### Python Setup

1. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix/Mac:
     ```bash
     source venv/bin/activate
     ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Node Setup

1. Install [Node.js](https://nodejs.org/) if not installed.
2. Install Node dependencies by running:
   ```bash
   npm install
   ```

## Running the Application

### Using Electron (Desktop App)

1. Ensure Python dependencies are installed (see Python Setup above).
2. Start the Electron application with:
   ```bash
   npm start
   ```
   This will spawn the Flask server (via `base.py`) and open an Electron window pointing to the ToDo app at [http://127.0.0.1:51140](http://127.0.0.1:51140).

### Running Flask Alone (Web Server Only)

If you want to run just the Flask server without Electron, execute:
   ```bash
   python base.py
   ```
Then open your browser at [http://127.0.0.1:51140](http://127.0.0.1:51140).

## Troubleshooting

- Ensure that all Python dependencies are properly installed.
- Verify that the Flask server works by running `python base.py` and accessing it via your browser.

## Packaging for Distribution

For creating a Windows desktop executable, consider using tools like:
- [Electron Packager](https://github.com/electron/electron-packager)
- [Electron Builder](https://www.electron.build/)

These tools can bundle the entire application, including the Python backend, into a standalone executable.

## License

This project is licensed under the MIT License.
