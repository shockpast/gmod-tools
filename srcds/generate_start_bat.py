from datetime import datetime
import os
import platform
import time
import sys

try:
    import colorama
except ImportError:
    print("colorama not installed!")

try:
    import cpuinfo
except ImportError:
    print("cpuinfo not installed!")

info_log    = f"{colorama.Fore.BLUE}[INFO]{colorama.Style.RESET_ALL}"
input_log   = f"{colorama.Fore.LIGHTBLUE_EX}[INPUT]{colorama.Style.RESET_ALL}"
warn_log    = f"{colorama.Fore.YELLOW}[WARN]{colorama.Style.RESET_ALL}"
error_log   = f"{colorama.Fore.RED}[ERROR]{colorama.Style.RESET_ALL}"
success_log = f"{colorama.Fore.GREEN}[SUCCESS]{colorama.Style.RESET_ALL}"
wait_log    = f"{colorama.Fore.CYAN}[WAIT]{colorama.Style.RESET_ALL}"

current_time = datetime.now().strftime("%H:%M:%S")

clear = lambda: os.system("cls")
clear()

"""
    Port.
"""
print(f"[{current_time}] | {info_log} Name: Port [*].")
print(f"[{current_time}] | {info_log} Description: The port the server will run on.")
print(f"[{current_time}] | {info_log} Arguments: integer (e.g. 27015)")
port = int(input(f"[{current_time}] | {input_log} Value: "))

if (not type(port) is int):
    print(f"[{current_time}] | {error_log} server.port must be an integer!")
    raise SystemExit

elif (port <= 0 or port == ""):
    print(f"[{current_time}] | {error_log} server.port must be something, like an example!")
    raise SystemExit

clear()

"""
    Tickrate.
"""
print(f"[{current_time}] | {info_log} Name: Tick Rate [*].")
print(f"[{current_time}] | {info_log} Description: The tick rate the server will run. Higher the number, more demanding it is on the CPU. A performant tickrate is around 30. Max: 128.")
print(f"[{current_time}] | {info_log} Arguments: integer (e.g. 33)")
tickrate = int(input(f"[{current_time}] | {input_log} Value: "))

if (not type(tickrate) is int):
    print(f"[{current_time}] | {error_log} server.tickrate must be an integer!")
    raise SystemExit

elif (tickrate < 16 or tickrate > 128):
    print(f"[{current_time}] | {error_log} server.tickrate can't be lower than 16 or higher than 128!")
    raise SystemExit

clear()

"""
    LAN Server -> sv_lan 0/1.
"""
print(f"[{current_time}] | {info_log} Name: LAN Server [*].")
print(f"[{current_time}] | {info_log} Description: LAN servers only allow users from your local network to connect. Public servers will require you to port forward your server's port number.")
print(f"[{current_time}] | {info_log} Arguments: integer (e.g. 0)")
lan = int(input(f"[{current_time}] | {input_log} Value: "))

if (not type(lan) is int):
    print(f"[{current_time}] | {error_log} server.lan must be an integer!")
    raise SystemExit

elif (lan < 0 or lan > 1):
    print(f"[{current_time}] | {error_log} server.lan can't be lower than 0 or higher than 1!")
    raise SystemExit

elif (lan == 1):
    print(f"[{current_time}] | {warn_log} server.lan = 1, it may not appear in your server browser!")
    print(f"[{current_time}] | {info_log} Press [ENTER] to continue generation.")
    input("")

clear()

"""
    Max Players.
"""
print(f"[{current_time}] | {info_log} Name: Max Players [*].")
print(f"[{current_time}] | {info_log} Description: The max amount of players that can play on this ")
print(f"[{current_time}] | {info_log} Arguments: integer (e.g. 128)")
max_players = int(input(f"[{current_time}] | {input_log} Value: "))

if (not type(max_players) is int):
    print(f"[{current_time}] | {error_log} server.max_players must be an integer!")
    raise SystemExit

elif (max_players <= 0 or max_players > 128):
    print(f"[{current_time}] | {error_log} server.max_players can't be lower than 1 or higher than 128!")
    raise SystemExit

clear()

"""
    Gamemode.
"""
print(f"[{current_time}] | {info_log} Name: Gamemode [*].")
print(f"[{current_time}] | {info_log} Description: The name of your gamemode's folder.")
print(f"[{current_time}] | {info_log} Arguments: string (e.g. sandbox)")
gamemode = str(input(f"[{current_time}] | {input_log} Value: "))

if (not type(gamemode) is str):
    print(f"[{current_time}] | {error_log} server.gamemode must be an string!")
    raise SystemExit

elif (gamemode == ""):
    print(f"[{current_time}] | {error_log} server.gamemode can't be blank!")
    raise SystemExit

clear()

"""
    Map.
"""
print(f"[{current_time}] | {info_log} Name: Map [*].")
print(f"[{current_time}] | {info_log} Description: The name of the map the server will run, must be included in your server files.")
print(f"[{current_time}] | {info_log} Arguments: string (e.g. gm_construct)")
map = str(input(f"[{current_time}] | {input_log} Value: "))

if (not type(map) is str):
    print(f"[{current_time}] | {error_log} server.map must be an string!")
    raise SystemExit

elif (map == ""):
    print(f"[{current_time}] | {error_log} server.map can't be blank!")
    raise SystemExit

clear()

"""
    Workshop Collection ID.
"""
print(f"[{current_time}] | {info_log} Name: Workshop Collection ID - skip.")
print(f"[{current_time}] | {info_log} Description: It will skip adding of \"Workshop Collection ID\".")
print(f"[{current_time}] | {info_log} Arguments: string")
workshop_add = str(input(f"[{current_time}] | {input_log} Add (Y/N): "))

if (workshop_add == "Y"):
    print(f"[{current_time}] | {info_log} Name: Workshop Collection ID - add.")
    print(f"[{current_time}] | {info_log} Description: The ID your steam workshop collection. This will be the addons the server automatically downloads. (Clients will not download these files)")
    print(f"[{current_time}] | {info_log} Arguments: integer (e.g. 2594826718)")
    workshop = int(input(f"[{current_time}] | {input_log} Value: "))

    if (not type(workshop) is int):
        print(f"[{current_time}] | {error_log} server.workshop must be an int!")
        raise SystemExit

    clear()

else:
    workshop = ""

    clear()

"""
    start.bat creating process.
"""
try:
    print(f"[{current_time}] | {wait_log} Creating \"start.bat\"... [1/4]")

    create_start_bat = open("start.bat", "x")
    time.sleep(0.2) 

    print(f"[{current_time}] | {success_log} \"start.bat\" saved! [2/4]")

except FileExistsError:
    print(f"[{current_time}] | {error_log} \"start.bat\" already exists!")
    raise SystemExit

try:
    print(f"[{current_time}] | {wait_log} Writing all configurations into \"start.bat\"... [3/4]")

    port        = port
    tickrate    = tickrate
    lan         = lan
    max_players = max_players
    gamemode    = gamemode
    map         = map
    workshop    = workshop

    start_bat = open("start.bat", "a")
    start_bat.write(f"start \"SRCDS\" /B srcds.exe -game garrysmod -conlog -port {port} -console -conclearlog -condebug -tvdisable -maxplayers {max_players} +gamemode {gamemode} +map {map} +host_workshop_collection \"{workshop}\" -tickrate {tickrate} +fps_max {tickrate} +sv_lan {lan}\n:: Created via Garry's Mod Tools at {current_time}!")

    print(f"[{current_time}] | {success_log} \"start.bat\" successfully configured! [4/4]")
    raise SystemExit
except Exception as unknown_error:
    print(f"[{current_time}] | {warn_log} Whoops, unknown error!")
    print(f"[{current_time}] | {warn_log} Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    file_time = datetime.now().strftime("%H.%M.%S")

    try:
        create_error_log = open(f"error-{file_time}.log", "x")
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        error_log = open(f"error-{file_time}.log", "a")
        error_log.write(f"""Whoops! That's an error!
        \n--------------------------------------------------\n
        Type: {exc_type}\n
        File: {fname}\n
        Line: {exc_tb.tb_lineno}\n
        Detailed Error: {unknown_error}
        \n--------------------------------------------------\n
        OS: {sys.platform}\n
        CPU: {cpuinfo.get_cpu_info()['brand']}\n
        Python: {platform.python_version}""")

        raise SystemExit
    except FileExistsError:
        print(f"[{current_time}] | {error_log} \"error-{file_time}.log\" already exists!")
        raise SystemExit