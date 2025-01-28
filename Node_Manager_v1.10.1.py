#For Reference
#https://github.com/FreedomCoin-Project/FreedomCoin-Core/releases/tag/5.4.0.0
#https://github.com/FreedomCoin-Project/FreedomCoin-Core
#https://github.com/FreedomCoin-Project/FreedomCoin-Core/wiki/Multi-Patriotnodes-on-VPS-Ubuntu-64bit-Setup-Guide

#IE needs absolute path
#/home/username/FreedomCoin/Freed1/freedomcoin-cli -datadir=/home/username/FreedomCoin/Freed1 getinfo
#f"{file_path} datadir={file_path} getinfo"
 
#Commands examples
"""
./freedomcoind -datadir=./
./freedomcoin-cli -datadir=./ getinfo
./freedomcoin-cli -datadir=./ stop
rm debug.log wallet.dat #maybe not this
./freedomcoin-cli -datadir=./ getpatriotnodestatus
"""

# Import the necessary module
import tkinter as tk
from tkinter import ttk
import subprocess
import os
import requests
import zipfile
import shutil
from idlelib.tooltip import Hovertip
import platform
from threading import Timer
import configparser
from functools import partial
import threading
import re
import time
import requests
from tkinter import filedialog, messagebox

os.chdir(os.path.expanduser("~"))
Home=os.getcwd()
#print(Home)
#print(os.getcwd())
#FreedomCoin=os.getcwd()
directory_path = "FreedomCoin"


file_path = "alert.txt"
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        pass  # The file will be created if it doesn't exist

def is_freedomcoin():
    freedom_zipfile = "FreedomCoin-Core-Linux.zip"
    if not os.path.isfile(freedom_zipfile):
        print("FreedomCoin-Core-Linux.zip does not exist")
        get_freedomcoin()
        unzip_freedomcoin()
        get_bootstrap()
        unzip_bootstrap()
        create_first_node("FreedomCoin") #copies bootstrap files

    else:
        #create_another_node("FreedomCoin")
        progress_label=tk.Label(window, text="Checking Requirements", bg=freedbg, fg=freedfg, font=freedfont)
        progress_label.place(y=45, x=275)
        window.after(3000, progress_label.destroy)
        t= Timer(3, is_bootstrap)
        t.start()
        

def is_bootstrap():
    bootstrap_zipfile = "bootstrap.zip"
    if not os.path.isfile(bootstrap_zipfile):
        print("bootstrap.zip does not exist")

    else:
        progress_label=tk.Label(window, text="Status Check OK", bg=freedbg, fg=freedfg, font=freedfont)
        progress_label.place(y=45, x=275)
        window.after(3000, progress_label.destroy)

def get_freedomcoin():
    #os.chdir("FreedomCoin")
        url = "https://github.com/FreedomCoin-Project/FreedomCoin-Core/releases/download/5.4.0.0/FreedomCoin-Core-Linux.zip"
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length'))
        downloaded = 0
        # Check if the request was successful
        if response.status_code == 200:
            progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
            progress_bar.place(y=17, x=275)
            progress_label=tk.Label(window, text="Downloading\n FeedomCoin-Core-Linux.zip", bg=freedbg, fg=freedfg, font=freedfont)
            progress_label.place(y=45, x=275)
            with open("FreedomCoin-Core-Linux.zip", "wb") as f:
                for chunk in response.iter_content(chunk_size=16384):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress_bar["value"] = (downloaded / total_length) * 100
                        progress_bar.update()
                progress_bar.destroy()
                progress_label.destroy()
        else:
            print(f"Error downloading file: {response.status_code}")

def get_bootstrap():
    #os.chdir("FreedomCoin")
        url = "https://freedomcoin.global/wallets/bootstrap.zip"
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length'))
        downloaded = 0
        # Check if the request was successful
        if response.status_code == 200:
            progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
            progress_bar.place(y=17, x=275)
            progress_label=tk.Label(window, text="Downloading\n bootstrap.zip", bg=freedbg, fg=freedfg, font=freedfont)
            progress_label.place(y=45, x=275)
            with open("bootstrap.zip", "wb") as f:
                for chunk in response.iter_content(chunk_size=16384):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress_bar["value"] = (downloaded / total_length) * 100
                        progress_bar.update()
                progress_bar.destroy()
                progress_label.destroy()
        else:
            print(f"Error downloading file: {response.status_code}")

def unzip_freedomcoin():
    os.chdir(os.path.expanduser("~"))
    freedom_zipfile = "FreedomCoin-Core-Linux.zip"
    files_to_extract =['freedomcoin-cli', 'freedomcoind']

    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(y=17, x=275)
    progress_label=tk.Label(window, text="Unzipping\n FeedomCoin-Core-Linux.zip", bg=freedbg, fg=freedfg, font=freedfont)
    progress_label.place(y=45, x=275)
    with zipfile.ZipFile(freedom_zipfile, 'r') as zip_ref:
        total_files = len(zip_ref.infolist())
        progress_bar["maximum"] = total_files

        for i, file in enumerate(zip_ref.infolist()):
            #if file in files_to_extract:
            zip_ref.extract(file)
            progress_bar["value"] = i + 1
            window.update_idletasks()
        progress_bar.destroy()
        progress_label.destroy()

def unzip_bootstrap():
    os.chdir(os.path.expanduser("~"))
    boot_zipfile = "bootstrap.zip"
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(y=17, x=275)
    progress_label=tk.Label(window, text="Unzipping\n bootstrap.zip", bg=freedbg, fg=freedfg, font=freedfont)
    progress_label.place(y=45, x=275)
    with zipfile.ZipFile(boot_zipfile, 'r') as zip_ref:
        total_files = len(zip_ref.infolist())
        progress_bar["maximum"] = total_files

        for i, file in enumerate(zip_ref.infolist()):
            zip_ref.extract(file)
            progress_bar["value"] = i + 1
            window.update_idletasks()
        progress_bar.destroy()
        progress_label.destroy()            
      
def create_first_node(path):
    src ="bootstrap"
    dest="FreedomCoin/Freed1"
    print(src,dest)
    # Count total files to copy
    total_files = sum([len(files) for _, _, files in os.walk(src)])

    # Create progress bar
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(y=17, x=275)
    progress_label=tk.Label(window, text="Creating First Node\nFreedomCoin\nFreed1", bg=freedbg, fg=freedfg, font=freedfont)
    progress_label.place(y=45, x=275)

    def copy_tree_wrapper(src, dest):
        nonlocal progress_bar
        copied_files = 0

        def copy_file(src, dest):
            nonlocal copied_files
            shutil.copy(src, dest)
            copied_files += 1
            progress_bar["value"] = (copied_files / total_files) * 100
            window.update_idletasks()

        shutil.copytree(src, dest, copy_function=copy_file)
        progress_bar.destroy()
        progress_label.destroy()
        copy_freedomcoin_files("FreedomCoin/Freed1")
        remove_unwanted_items()
        #first run args for first create_config()
        path=dest
        rpcuser="userFreed1"
        rpcpass="passFreed1"
        rpcport="10001"
        make_executables()
        create_config(path,rpcuser, rpcpass,rpcport)
        
    # Copy files in a separate thread
    #import threading
    threading.Thread(target=copy_tree_wrapper, args=(src, dest)).start()   

# Creates first trumpcoin.conf
def create_config(path, rpcuser, rpcpass, rpcport):
    
    config = configparser.ConfigParser()
    
    # Add sections and key-value pairs

    config['DEFAULT'] = {'rpcuser':f'{rpcuser}',
                    'rpcpassword':f'{rpcpass}',
                    'rpcallowip':'127.0.0.1',
                    'server':'1',
                    'daemon':'1',
                    'patriotnode':'1',
                    'rpcport':f'{rpcport}',
                    'patriotnodeprivkey':'Results of Step 1',
                    'patriotnodeaddr':'YOURVPSIP:15110',
                    'listen':'0'}

    # Write the configuration to a file
    folder_path =f"{path}"
    file_name = "trumpcoin.conf"
    file_path = os.path.join(folder_path, file_name)
    print(file_path)
    with open(file_path, 'w') as configfile:
        for key, value in config['DEFAULT'].items():
            configfile.write(f'{key}={value}\n')

# Finding files/folders
def find_files(filename, root_dir): 
    matching_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d != "Trash"]
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for file in files:
            if file == filename:
                matching_files.append(os.path.join(root, file))
    return matching_files

# Find files/folders with certain file aka trumpcoin.conf files.
def change_ip(ip):
    
    filename_to_search = "trumpcoin.conf"
    root_directory = Home

    found_files = find_files(filename_to_search, root_directory)
    config = configparser.ConfigParser()

#Read, then set IP without headers or sections.        
    for file_path in found_files:
        print(file_path)
        with open(f'{file_path}', 'r') as f:
            config.read_string('[DEFAULT]\n' + f.read())
            for key, value in config['DEFAULT'].items():
                config.set('DEFAULT', 'patriotnodeaddr', f'{ip}:15110')
                #print(key,"=",value)                
                with open(file_path, 'w') as configfile:
                    for key, value in config['DEFAULT'].items():
                        configfile.write(f'{key}={value}\n')               
    
# Create IP objects and get entry value for change ip
def create_entry_objects():
    
    global entry_label2
    def get_entry_value():
        global entry_label2
        ip = entry_ip.get()
        print("Entry value:", ip)        
        entry_label2 = tk.Label(window, text=f"(Patriotnodes) set to {ip}", bg=freedbg, fg=freedfg, font=freedfont)
        entry_label2.place(y=15, x=298)
        change_ip(ip)
        submit_button.config(state= "disabled")
        
    def close_and_destroy():
        global entry_label2
        entry_label.destroy()
        entry_ip.destroy()
        submit_button.destroy()
        close_button.destroy()
        button_num[1].config(state = "normal")

        try:
            entry_label2.destroy()
        except:
            print("no such label, exception handled")
    
    entry_label = tk.Label(window, text="Change (ALL) IP's", bg=freedbg, fg=freedfg, font=freedfont)
    entry_label.place(y=125, x=25)
    entry_ip = tk.Entry(window, bg=freedbg, fg=freedfg, font=freedfont)
    entry_ip.place(y=150)
    submit_button = tk.Button(window, text="Submit", activebackground="goldenrod", bg=freedbg, command=get_entry_value)
    submit_button.place(y=147, x=210)
    close_button = tk.Button(window, text=" Close ", activebackground="goldenrod", bg=freedbg, command=close_and_destroy)
    close_button.place(y=147, x=285)

#needs work
def manage_nodes():
    #global labels
    #print(labels)
    filename_to_search = "freedomcoin-cli"
    root_directory = Home
    node_y=200
    node_x=1
    
    found_files = find_files(filename_to_search, root_directory)
# For Reference command syntax
# ("/home/steve12/FreedomCoin/Freed1/freedomcoin-cli -datadir=/home/steve12/FreedomCoin/Freed1 getinfo")
#--------------------------------------------------------NEEDS WORK - total revamp function for buttons colors.
    def commands(c_path, x_com=None):
        nonlocal status_list
        if x_com is None:
            command= (f"{c_path}")
            #print(command)
        else:
            command= (f"{c_path} {x_com}")

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("OK", result.stdout)
        else:
            print("Error:\n" + result.stderr)
        
        for key, value in status_list.items():
            if value == command:
                if "Patriotnode successfully started" in result.stdout:
                    #print(key)
                    #print(value)
                    status_num[key].config(activebackground="chartreuse3", bg="chartreuse2")
                    #print(status_num[key])
                    #print(node_label[key]["text"], "OK")
                    data=f"{node_label[i]['text']}= ON"
                    break
                else:
                    #print(node_label[key]["text"], "OFF")
                    status_num[key].config(activebackground="firebrick3", bg="firebrick2")
                    data=f"{node_label[i]['text']}= OFF"
                    off_message(data)
        
    def start_thread(new_com, x_com=None):#for (start_buttons) commands only because the program doesn't stop running. 
        #print(new_com, x_com)
        thread= threading.Thread(target=commands, args=(f"{new_com}", x_com))
        thread.start()
  
    def monitor():
        while True:
            for i in range(len(status_num)):
                status_num[i].invoke()
                time.sleep(20)
                
                if status_num[i]["bg"]=="firebrick2":
                    for i in range(len(status_num)):
                        if status_num[i]["bg"]=="chartreuse2":
                            print(node_label[i]["text"], "OK")
                            
                        else:
                            print(node_label[i]["text"], "OFF")
            break        
                            
    def thread_monitor():
        thread= threading.Thread(target=monitor)
        thread.start()
        
    def off_message(data):
        with open("alert.txt", "r") as file:
            alert = file.read()
            #print("alert file", alert)
            
        requests.post(f"https://ntfy.sh/{alert}",
        data=f"{data}",
            headers={
                "Title": "Patriotnode Alert",
                "Priority": "5",
                "Tags": "rotating_light",
                })
        
    def on_message(data):
        requests.post(f"https://ntfy.sh/{alert}",
        data=f"{data}",
            headers={
                "Title": "Patriotnode Alert",
                "Priority": "5",
                "Tags": "rotating_light",
                })

    def config_window(conf_path): #child window
        print(conf_path)
        
        def load_config(conf_path):
            """Loads the config file and populates the entry fields."""
            #global config_file_path
            #config_file_path = filedialog.askopenfilename(defaultextension=".conf")
            config_file_path= f"{conf_path}"
            #print(config_file_path)
            if not config_file_path:
                return  # No file selected

            #config.read(config_file_path)

            with open(f'{config_file_path}', 'r') as f:
                config.read_string('[DEFAULT]\n' + f.read())
                for key, value in config['DEFAULT'].items():
                    #print(value)
                    if key in entry_fields:
                        entry_fields[key].delete(0, tk.END)
                        entry_fields[key].insert(0, config["DEFAULT"][key])


        def save_config(conf_path):
            """Saves the updated config values to the file."""
            for key in entry_fields:
                config["DEFAULT"][key] = entry_fields[key].get()

            with open(f"{conf_path}", "w") as configfile:
                for key, value in config['DEFAULT'].items():
                    configfile.write(f'{key}={value}\n')

            messagebox.showinfo("Success", "Config file saved.")
        
        
        
        # Create the child window
        child_window = tk.Toplevel(window)
        child_window.geometry("400x400")
        child_window.title("Configure trumpcoin.conf")

        # Create the config parser
        config = configparser.ConfigParser()

        # Create entry fields for config values
        entry_fields = {}
        for key in ["rpcuser", "rpcpassword","rpcallowip",\
            "server", "daemon", "patriotnode",\
            "rpcport",\
            "patriotnodeprivkey", "patriotnodeaddr",\
            "listen"]:
            # Add more keys as needed

            label = tk.Label(child_window, text=key)
            label.grid(row=len(entry_fields), column=0)
            entry = tk.Entry(child_window)
            entry.grid(row=len(entry_fields), column=1)
            entry_fields[key] = entry

        # Create buttons
        #load_button = tk.Button(child_window, text="Load Config", command= lambda: load_config(conf_path))
        #load_button.grid(row=len(entry_fields), column=0, columnspan=2)

        save_button = tk.Button(child_window, text="Save Config", command= lambda: save_config(conf_path))
        save_button.grid(row=len(entry_fields) + 1, column=0, columnspan=2)

        load_config(conf_path)
        
    node_label=[]
    status_num  = []       
    status_list = {}
    for i, file_path in enumerate(found_files):
        #print(i,file_path)
        status_num.append(i) #add index to list
        node_label.append(i)
        node_dir=os.path.dirname(file_path)
        subdirname = os.path.basename(os.path.dirname(file_path))
        c_path = f"{file_path} -datadir={node_dir}"
        new_path=os.path.join(os.path.dirname(file_path), "freedomcoind")
        new_com= f"{new_path} -datadir={node_dir}"
        conf_path=new_path=os.path.join(os.path.dirname(file_path), "trumpcoin.conf")
        #print("path ",conf_path)
        node_label[i] = tk.Label(window, text=subdirname, bg=freedbg, fg=freedfg, font=freedfont)
        node_label[i].place(y=node_y, x=node_x)
        start_button = tk.Button(window, text="Start", activebackground="goldenrod", bg=freedbg, command=partial(start_thread, f"{new_com}"))
        start_button.place(y=node_y-3, x=node_x+125)
        stop_button = tk.Button(window, text="Stop", activebackground="goldenrod", bg=freedbg, command=partial(commands, f"{c_path}","stop"))
        stop_button.place(y=node_y-3, x=node_x+185)
        config_button = tk.Button(window, text="Config", activebackground="goldenrod", bg=freedbg, command=partial(config_window, f"{conf_path}"))
        config_button.place(y=node_y-3, x=node_x+243)
        get_info= tk.Button(window, text="Get Info", activebackground="goldenrod", bg=freedbg, command=partial(commands, f"{c_path}","getinfo"))
        get_info.place(y=node_y-3, x=node_x+314)
        status_num[i] = tk.Button(window, text="Status", activebackground="goldenrod", bg=freedbg, command=partial(commands, f"{c_path}","getpatriotnodestatus")) # RE: status
        status_num[i].place(y=node_y-3, x=node_x+395)# RE: assign item to index
        status_list[i]=f"{c_path} getpatriotnodestatus" #dictionary key matches list index
        #print(status_list)
        node_y=node_y+35
        commands(f"{c_path}","getpatriotnodestatus")
    thread_monitor()
        
# Copy after creating first node
def copy_freedomcoin_files(path):
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(y=17, x=275)
    src_dir = "FreedomCoin-Core-Linux"
    dest_dir = "FreedomCoin/Freed1"
    file_names_to_copy =['freedomcoin-cli', 'freedomcoind']
    for file_name in os.listdir(src_dir):
            if file_name in file_names_to_copy:
                
                #print(f"{src_dir}/{file_name}")
                src=f"{src_dir}/{file_name}"
                dest=f"{dest_dir}/{file_name}"
                progress_label=tk.Label(window, text=f"Moving File {file_name}", bg=freedbg, fg=freedfg, font=freedfont)
                progress_label.place(y=45, x=275)
    
                total_size = os.path.getsize(src)
                copied_size = 0
                progress_bar["value"] = 0

                with open(src, "rb") as fsrc, open(dest, "wb") as fdest:
                    while True:
                        chunk = fsrc.read(4096)  # Adjust chunk size if needed
                        if not chunk:
                            break

                        fdest.write(chunk)
                        copied_size += len(chunk)
                        progress_bar["value"] = (copied_size / total_size) * 100
                        window.update_idletasks()
                progress_label.destroy()

    progress_bar["value"] = 100
    progress_bar.destroy()
    progress_label.destroy()

def remove_unwanted_items():
    directories_to_delete = ["FreedomCoin-Core-Linux", "bootstrap", "__MACOSX"]
    files_to_delete = ["FreedomCoin-Core-Linux.zip", "bootstrap.zip"]
    if os.path.isdir("FreedomCoin-Core-Linux")or os.path.isdir("boostrap")\
       or os.path.isdir("__MACOSX"):
        for directory in directories_to_delete:
            progress_label=tk.Label(window, text=f"Removing {directory}", bg=freedbg, fg=freedfg, font=freedfont)
            progress_label.place(y=45, x=275)
            shutil.rmtree(directory)
            progress_label.destroy()
     
    else:
        print("no such directory")

    if os.path.isfile("bootstrap.zip")or os.path.isfile("FreedomCoin-Core-Linux.zip"):
        for file_name in os.listdir():
            if file_name in files_to_delete:
                os.remove(file_name)
    else:
        print("no such files")

# Create More Nodes
# Copies previous NODE files only
# Does NOT download (FreedomCoin-Core-Linux.zip or bootstrap.zip)
def create_another_node(src, dest, rpcuser, rpcpass, rpcport, new_node, node_count):
    """
    Nodes=[]
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            Nodes.append(entry)
    Freed="Freed"+str(len(Nodes)+1)
    Nodes.append(Freed)
    """
    #src = f"{path}"
    #dest=f"{path}"
    #print("Node Count= ",len(Nodes),f" {Nodes}")
    #new_node = re.sub(r'\d+$', '', subdirname)+ str(node_count)
    print(src,dest)
    # For create_config()
    #userpass = "User"+subdirname
    #rpcport_num = len(node_count)
    # Count total files to copy
    total_files = sum([len(files) for _, _, files in os.walk(src)])

    # Create progress bar
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress_bar.place(y=17, x=275)
    progress_label=tk.Label(window, text=f"Creating Patriotnode\n{new_node}\nNode Count= ({node_count})", bg=freedbg, fg=freedfg, font=freedfont)
    progress_label.place(y=45, x=275)

    def copy_tree_wrapper(src, dest):
        nonlocal progress_bar
        copied_files = 0

        def copy_file(src, dest):
            nonlocal copied_files
            shutil.copy(src, dest)
            copied_files += 1
            progress_bar["value"] = (copied_files / total_files) * 100
            window.update_idletasks()

        shutil.copytree(src, dest, copy_function=copy_file)
        progress_bar.destroy()
        progress_label.destroy()
        create_config(dest, rpcuser, rpcpass, rpcport)
        
    # Copy files in a separate thread
    import threading
    threading.Thread(target=copy_tree_wrapper, args=(src, dest)).start()

# Checks if FreedomCoin exists and downloads .zips, unzips and creates first node
# else creates another node without requiring new downloads of .zips or unzipping etc. 
def if_nodes_exist():
    filename_to_search = "freedomcoin-cli"
    root_directory = Home
    found_files = find_files(filename_to_search, root_directory)
    node_count = len(found_files)+1
    if len(found_files) >0:
       
        for file_path in (found_files):
            src=os.path.dirname(file_path)
            dest=re.sub(r'\d+$', '', src)+ str(node_count) #remove ending numbers, add node_count for folder naming.
        
        subdirname = os.path.basename(os.path.dirname(file_path))
        new_node= re.sub(r'\d+$', '', subdirname)+ str(node_count) # for label during creation 
        rpcuser = "user"+re.sub(r'\d+$', '', subdirname)+ str(node_count)
        rpcpass = "pass"+re.sub(r'\d+$', '', subdirname)+ str(node_count)
        rpcport=10000+node_count
        print(len(found_files), " patriotnodes found")
        #print(src, dest, rpcuser, rpcpass)
        #print(subdirname)
        create_another_node(src, dest, rpcuser, rpcpass, rpcport, new_node, node_count)

    else:
        print("no nodes found -installing first node")
        is_freedomcoin()

def make_executables():
    filename_to_search = "freedomcoind"
    root_directory = Home
    found_files = find_files(filename_to_search, root_directory)
    if len(found_files)>0:
        for file_path in (found_files):
            print("set permissions 0o755 ", file_path)
            os.chmod(file_path, 0o755)
        filename_to_search = "freedomcoin-cli"
        found_files = find_files(filename_to_search, root_directory)
        for file_path in (found_files):
            print("set permissions 0o755 ", file_path)
            os.chmod(file_path, 0o755)
    else:
        print("no files found to set permissions")
      
def alert_sub():
    
    global entry_label2
    def get_entry_value():
        global entry_label2
        alert = entry_alert.get()
        print("Entry value:", alert)        
        entry_label2 = tk.Label(window, text=f"Sending to {alert}", bg=freedbg, fg=freedfg, font=freedfont)
        entry_label2.place(y=15, x=298)
        with open("alert.txt", "w") as f:
            f.write(alert)
        submit_button.config(state= "disabled")
        
    def close_and_destroy():
        global entry_label2
        entry_label.destroy()
        entry_alert.destroy()
        submit_button.destroy()
        close_button.destroy()
        button_num[2].config(state = "normal")

        try:
            entry_label2.destroy()
        except:
            print("no such label, exception handled")

    entry_label = tk.Label(window, text="(Subscription Name)", bg=freedbg, fg=freedfg, font=freedfont)
    entry_label.place(y=55, x=280)
    entry_alert = tk.Entry(window, bg=freedbg, fg=freedfg, font=freedfont)
    entry_alert.place(y=85, x=260)
    submit_button = tk.Button(window, text="Submit", activebackground="goldenrod", bg=freedbg, command=get_entry_value)
    submit_button.place(y=82, x=470)
    close_button = tk.Button(window, text=" Close ", activebackground="goldenrod", bg=freedbg, command=close_and_destroy)
    close_button.place(y=82, x=546)


            
#reminder to len(stdout) and trim strings with \n for comparisons
def run_com1():
    command = if_nodes_exist()
     
def run_com2():
    command = create_entry_objects()
    button_num[1].config(state = "disabled")

def run_com3():
    command = alert_sub()
    button_num[2].config(state= "disabled")

# Create a Tkinter window
window = tk.Tk()
window.geometry("720x720")
window.title("FreedomCoin Patriotnode Manager")


# Define labels and buttons
labels = ["Install Patriotnode","Change IP", "Phone Alert Settings"]
buttons = ["Run", "Run", "Run"]
label_num=[]
button_num=[]
coms=[run_com1,run_com2,run_com3]
freedbg="light goldenrod"
freedfont=("MATHJAX+MATH", "12", "italic")
freedfg="black"

text_y=15 #vertical
text_x=1 #horizontal
button_y=12 
button_x=200
# Iterate over the labels and buttons - *I may change button to create button numbers for easy button text.config
for i in range(len(labels)):

    # Create a Label and Button widgets for each and put them in a list index for future referencing with .config
    label_num.append(i)
    button_num.append(i)
    label_num[i] = tk.Label(window, text=labels[i], bg=freedbg, fg=freedfg, font=freedfont)
    label_num[i].place(y=text_y)
    button_num[i] = tk.Button(window, text=buttons[i], activebackground="goldenrod", bg=freedbg, command=coms[i])
    button_num[i].place(y=button_y, x=button_x)
    text_y = text_y +35
    button_y= button_y +35

# mouse over Hovertips for buttons
mytip0 =Hovertip(button_num[0],
"\t         CREATE YOUR FIRST\n\t\
(FREEDOMCOIN PATRIOTNODE)\n\t\t\
   OR\n\t\
ADD A NEW PATRIOTNODE\n\t\
*no changes to existing folder structure\n\t\
*manage or add new nodes to existing folder\n\
SUMMERIZED:\n\
1-Create Folders (FreedomCoin/Freed1)\n\
2-Download (FreedomCoin-Core-Linux.zip)\n\
3-Download (bootstrap.zip)\n\
4-Extract (zip files)\n\
5-Copy required Files/Folders to (Freed1)\n\
6-Remove (Non-Required Files/Folders)\n\
8-Edit 1st Patriot Node Configuration File\n\
9-Start New Patriot Node and Check Status\n\
* buttons status\n\
   auto updates every 20 seconds")
mytip1 =Hovertip(button_num[1],
"Change (IP's) for (ALL) Patriotnodes\n\
Run,Submit and Close")
mytip2 =Hovertip(button_num[2],
"Phone Alert Settings\nSubscription Name\n\
 1. Download ntfy phone app\n\
 2. Android or Apple\n\
 3. On your phone add the (subscription name)\n\
 4. AND (On This APP) add the (subscription name)\n\
 5. Run, Submit and Close\n\
    turn off optimal energy saving for this app on your phone")
make_executables()
manage_nodes()
window.mainloop()
