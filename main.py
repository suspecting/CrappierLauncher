import tkinter as tk
from tkinter import ttk
import base64
import sys
from subprocess import Popen, PIPE
import logging

window = tk.Tk()
window.geometry("500x300")
window.configure(bg='purple')
Message = tk.Label(text="Checking if Crapblox exists", bg='purple', font=('Arial',20))
Message.place(x=10,y=260)
path = 'D:\client\\'

inp = sys.argv[1]
split_parsed = base64.b64decode(inp.split("://")[1]).decode("utf-8")

if sys.platform == 'linux':
    # Linux support is planned
    Message.config(text = "Linux support is planned")
    Message.place(x=10,y=260)
else:
    try:
        process = Popen([ path + 'CrapbloxPlayerBeta.exe',
                         '-a "https://crapblox.cf/"',
                         '-t 1',
                         'https://crapblox.cf/Game/JoinServer?Token=' + split_parsed.split(".")[1] + '&PlaceId=' + split_parsed.split(".")[0]],
                        stdout=PIPE,
                        stderr=PIPE)
        stdout, stderr = process.communicate()
        Message.config(text = "Joining...")
    except IndexError:
        Message.config(text = "U gotta do something else brother")
        pb = ttk.Progressbar(window, orient='horizontal', mode='determinate', length=480)
        pb.place(x=10,y=10)
        print("Gay")

window.mainloop()


