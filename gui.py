import tkinter as tk
from scanner import scan_port

# Function to run when Scan button is clicked
def start_scan():
    # Clear previous results
    result_box.delete("1.0", tk.END)

    # Get values from the input boxes
    target = ip_entry.get()
    start = start_entry.get()
    end = end_entry.get()

    # Display entered information
    result_box.insert(tk.END, f"Target IP: {target}\n")
    result_box.insert(tk.END, f"Start Port: {start}\n")
    result_box.insert(tk.END, f"End Port: {end}\n\n")
    result_box.insert(tk.END, "Scanning...\n")

# Create main window
window = tk.Tk()
window.title("Python Port Scanner")
window.geometry("600x500")
window.resizable(False, False)

# Heading
title = tk.Label(
    window,
    text="Python Port Scanner",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Target IP
ip_label = tk.Label(window, text="Target IP:")
ip_label.pack()

ip_entry = tk.Entry(window, width=30)
ip_entry.pack()

# Start Port
start_label = tk.Label(window, text="Start Port:")
start_label.pack()

start_entry = tk.Entry(window, width=30)
start_entry.pack()

# End Port
end_label = tk.Label(window, text="End Port:")
end_label.pack()

end_entry = tk.Entry(window, width=30)
end_entry.pack()

# Scan Button
import threading

scan_button = tk.Button(
    window,
    text="Scan",
    command=lambda: threading.Thread(target=start_scan).start()
)
scan_button.pack(pady=15)

# Results Box
result_box = tk.Text(window, height=15, width=70)
result_box.pack()

# Run GUI
window.mainloop()