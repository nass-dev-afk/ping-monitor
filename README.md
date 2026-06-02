# ping monitor in python


description:
very simple network monitor that checks if a host is online using ping utilities (CURRENTLY is only available on bash and zsh, but support for windows along with an expansion of general capabilites will probably be added later)

how it works:
script uses the Python `os` module to send a quiet single count ping (`ping -c 1`) to a specified hostname every 5 seconds
handles output redirection to keep the terminal clean and custom logs status messages

how to run it:
1.clone this repo or just download 'monitor.py'
2.run this script into your terminal:
```bash
   python3 monitor.py
```
3.to stop the script press crtl+c
