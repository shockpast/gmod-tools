from datetime import datetime

try:
    import colorama
except ImportError:
    print("colorama not installed!")

info_log    = f"{colorama.Fore.BLUE}[INFO]{colorama.Style.RESET_ALL}"
input_log   = f"{colorama.Fore.LIGHTBLUE_EX}[INPUT]{colorama.Style.RESET_ALL}"
warn_log    = f"{colorama.Fore.YELLOW}[WARN]{colorama.Style.RESET_ALL}"
error_log   = f"{colorama.Fore.RED}[ERROR]{colorama.Style.RESET_ALL}"
success_log = f"{colorama.Fore.GREEN}[SUCCESS]{colorama.Style.RESET_ALL}"
wait_log    = f"{colorama.Fore.CYAN}[WAIT]{colorama.Style.RESET_ALL}"

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