import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():

    long_url = entry.get()
    
    if long_url:
        short_url = shortener.tinyurl.short(long_url)
        output.config(text=short_url)
        pyperclip.copy(short_url)
    else:
        output.config(text="Enter the URL")

root = tk.Tk()
root.title("URL Shortener")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

shortener = pyshorteners.Shortener()

button = tk.Button(root, text="Shorten URL", command=shorten_url)
button.pack()

output = tk.Label(root, text="")
output.pack(pady=10)

copy_button = tk.Button(root, text="Copy URL", command=lambda: pyperclip.copy(output["text"]))
copy_button.pack()

root.mainloop()
