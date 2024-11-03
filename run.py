from threading import Thread
import os

def run_script(script):
    os.system(script)

scripts = [
    "python app.py",
    "npm run dev",
]

threads = []
for script in scripts:
    thread = Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()


    
