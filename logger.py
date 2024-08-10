from datetime import datetime
from colorama import Fore, init
import os

init(autoreset=True)

class Logger:
    def __init__(self, stack_mode=True, file_name="log.log",logs_folder="logs"):
        self.file_name = file_name
        self.stack_mode = stack_mode
        self.logs_folder_path = logs_folder
        
        if(self.stack_mode):
            if not os.path.exists(logs_folder):
                os.makedirs(logs_folder)
    
    def log(self, text = "log.log"):
        try:
            with open(self.file_name, "a") as f:
                f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), text))
                print(text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")

    def info(self, text= "log.log"):
        try:
            with open(self.file_name, "a") as f:
                f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[INFO] "  + text))
                print(Fore.BLUE + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")
    
    def err(self,text= "log.log",err_type=""):
        try:
            with open(self.file_name, "a") as f:
                if(err_type == "" or err_type == " "):
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[ERROR] "  + text))
                    print(Fore.RED + "[ERROR] " + text)
                else:
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[ERROR/" + err_type + "] "  + text))
                    print(Fore.RED + "[ERROR/" + err_type + "] " + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")

    def warn(self,text= "log.log",warn_type=""):
        try:
            with open(self.file_name, "a") as f:
                if(warn_type == "" or warn_type == " "):
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[WARNING] "  + text))
                    print(Fore.RED + "[WARNING] " + text)
                else:
                    f.write("[{0}] {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"),"[WARNING/" + warn_type + "] "  + text))
                    print(Fore.RED + "[WARNING/" + warn_type + "] " + text)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR/Logger] Log file or path not found!")
        except:
            print(Fore.RED + "[ERROR/Logger] An logger exception occurre")


