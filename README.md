# Remote Client Controller - Socket Application

## Description

This is a Python-based client-server application using **socket programming** that enables remote control and monitoring of a computer. The client GUI connects to a target IP and allows actions such as:

- Viewing running processes and applications  
- Logging keystrokes (keylogger)  
- Remote shutdown  
- Capturing screenshots  
- Terminating processes  
- Clean and intuitive GUI

---

## GUI Overview

### Main Client Interface

- **IP Entry**: Input the server's IP address to connect.
- **Connect Button**: Establish connection with the server.
- **Functional Buttons**:
  - `Process Running`: View all active processes.
  - `App Running`: View running applications (`.exe`).
  - `Keystroke`: Launch the keylogger panel.
  - `Shutdown`: Turn off the remote machine.
  - `Screenshot`: Capture the remote screen.
  - `Exit`: Close the application.

### Process & App Window

- Displays a list of running processes or applications with details:
  - **Process Name**
  - **Process ID (PID)**
  - **Thread Count**
- Features:
  - `Kill`: Terminate a selected process.
  - `View`: View details.
  - `Start`: Launch new process/app.
  - `Delete`: Remove from list view.

### Keystroke Logger

- **Hook**: Start keylogging.
- **Unhook**: Stop keylogging.
- **Print**: Display recorded keystrokes.
- **Clear**: Clear the log.

### Screenshot Window

- **Capture**: Take a screenshot of the remote screen.
- **Save**: Save the captured image locally.

---

## Requirements

- Python 3.x
- Required libraries:
  - `socket`
  - `tkinter`
  - `psutil`
  - `keyboard`
  - `pyautogui`
  - `Pillow`
  - `threading`, `subprocess`, `os`, `io`, etc.

Install dependencies using pip:

```bash
pip install psutil pyautogui keyboard pillow
