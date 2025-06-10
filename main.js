const { app, BrowserWindow } = require('electron');
const path = require('path');
app.commandLine.appendSwitch('no-sandbox');
const { spawn } = require('child_process');

let pyProc = null;
let win = null;

function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    title: 'ToDoアプリ',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  win.loadURL('http://127.0.0.1:9111');

  win.on('closed', () => {
    win = null;
  });
}

function startPython() {
  // Start the Flask backend
  pyProc = spawn('python', ['base.py']);

  pyProc.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
  });

  pyProc.stderr.on('data', (data) => {
    console.error(`Python stderr: ${data}`);
  });

  pyProc.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
  });
}

app.whenReady().then(() => {
  startPython();
  setTimeout(createWindow, 10000);

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Quit when all windows are closed, except on macOS
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
  if (pyProc) {
    pyProc.kill();
  }
});
