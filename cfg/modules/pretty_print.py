from datetime import datetime
import os

try:
    import colorama
except ImportError:
    print("colorama not installed!")

clear = lambda: os.system("cls")

info_log    = f"{colorama.Fore.LIGHTBLUE_EX}[INFO]{colorama.Style.RESET_ALL}"
input_log   = f"{colorama.Fore.LIGHTBLUE_EX}[INPUT]{colorama.Style.RESET_ALL}"
warn_log    = f"{colorama.Fore.LIGHTYELLOW_EX}[WARN]{colorama.Style.RESET_ALL}"
error_log   = f"{colorama.Fore.LIGHTRED_EX}[ERROR]{colorama.Style.RESET_ALL}"
success_log = f"{colorama.Fore.LIGHTGREEN_EX}[SUCCESS]{colorama.Style.RESET_ALL}"
wait_log    = f"{colorama.Fore.LIGHTCYAN_EX}[WAIT]{colorama.Style.RESET_ALL}"

current_time = datetime.now().strftime("%H:%M:%S")

def prettyinfo(arguments):
    return print(f"[{current_time}] | {info_log} {arguments}")

def prettyinput(arguments):
    return input(f"[{current_time}] | {input_log} {arguments}")

def prettyerror(arguments):
    return print(f"[{current_time}] | {error_log} {arguments}")

def prettywarn(arguments):
    return print(f"[{current_time}] | {warn_log} {arguments}")

def prettysuccess(arguments):
    return print(f"[{current_time}] | {success_log} {arguments}")

def prettywait(arguments):
    return print(f"[{current_time}] | {wait_log} {arguments}")

def askinput(name, description, arguments):
    prettyinfo("Name: " + name)
    prettyinfo("Description: " + description)
    prettyinfo("Arguments: " + arguments)

    receiver = input(f"[{current_time}] | {input_log} Value: ")

    clear()
    return receiver