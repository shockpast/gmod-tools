from datetime import datetime
import os
import platform
import time
import sys

# pip install ...
try:
    import cpuinfo
except ImportError:
    print("cpuinfo not installed!")

# External.
import print

clear = lambda: os.system("cls")
clear()

"""
    Port.
"""
print.prettyinfo("Name: Port [*].")
print.prettyinfo("Description: The port the server will run on.")
print.prettyinfo("Arguments: integer (e.g. 27015)")

port = int(print.prettyinput("Value: "))

if (not type(port) is int):
    print.prettyerror("server.port must be an integer!")

    raise SystemExit

elif (port <= 0 or port == ""):
    print.prettyerror("server.port must be something, like an example!")

    raise SystemExit

clear()

"""
    Tickrate.
"""
print.prettyinfo("Name: Tick Rate [*].")
print.prettyinfo("Description: The tick rate the server will run. Higher the number, more demanding it is on the CPU. A performant tickrate is around 30. Max: 128.")
print.prettyinfo("Arguments: integer (e.g. 33)")

tickrate = int(print.prettyinput("Value: "))

if (not type(tickrate) is int):
    print.prettyerror("server.tickrate must be an integer!")

    raise SystemExit

elif (tickrate < 16 or tickrate > 128):
    print.prettyerror("server.tickrate can't be lower than 16 or higher than 128!")

    raise SystemExit

clear()

"""
    LAN Server -> sv_lan 0/1.
"""
print.prettyinfo("Name: LAN Server [*].")
print.prettyinfo("Description: LAN servers only allow users from your local network to connect. Public servers will require you to port forward your server's port number.")
print.prettyinfo("Arguments: integer (e.g. 0)")

lan = int(print.prettyinput("Value: "))

if (not type(lan) is int):
    print.prettyerror("server.lan must be an integer!")

    raise SystemExit

elif (lan < 0 or lan > 1):
    print.prettyerror("server.lan can't be lower than 0 or higher than 1!")

    raise SystemExit

elif (lan == 1):
    print.prettywarn("server.lan = 1, it may not appear in your server browser!")
    print.prettyinfo("Press [ENTER] to continue generation.")

    input("")

clear()

"""
    Max Players.
"""
print.prettyinfo("Name: Max Players [*].")
print.prettyinfo("Description: The max amount of players that can play on this ")
print.prettyinfo("Arguments: integer (e.g. 128)")

max_players = int(print.prettyinput("Value: "))

if (not type(max_players) is int):
    print.prettyerror("server.max_players must be an integer!")

    raise SystemExit

elif (max_players <= 0 or max_players > 128):
    print.prettyerror("server.max_players can't be lower than 1 or higher than 128!")

    raise SystemExit

clear()

"""
    Gamemode.
"""
print.prettyinfo("Name: Gamemode [*].")
print.prettyinfo("Description: The name of your gamemode's folder.")
print.prettyinfo("Arguments: string (e.g. sandbox)")

gamemode = str(print.prettyinput("Value: "))

if (not type(gamemode) is str):
    print.prettyerror("server.gamemode must be an string!")

    raise SystemExit

elif (gamemode == ""):
    print.prettyerror("server.gamemode can't be blank!")

    raise SystemExit

clear()

"""
    Map.
"""
print.prettyinfo("Name: Map [*].")
print.prettyinfo("Description: The name of the map the server will run, must be included in your server files.")
print.prettyinfo("Arguments: string (e.g. gm_construct)")

map = str(print.prettyinput("Value: "))

if (not type(map) is str):
    print.prettyerror("server.map must be an string!")

    raise SystemExit

elif (map == ""):
    print.prettyerror("server.map can't be blank!")

    raise SystemExit

clear()

"""
    Workshop Collection ID.
"""
print.prettyinfo("Name: Workshop Collection ID - skip.")
print.prettyinfo("Description: It will skip adding of \"Workshop Collection ID\".")
print.prettyinfo("Arguments: string")

workshop_add = str(print.prettyinput("Add (Y/N): "))

if (workshop_add == "Y"):
    print.prettyinfo("Name: Workshop Collection ID - add.")
    print.prettyinfo("Description: The ID your steam workshop collection. This will be the addons the server automatically downloads. (Clients will not download these files)")
    print.prettyinfo("Arguments: integer (e.g. 2594826718)")
    workshop = int(print.prettyinput("Value: "))

    if (not type(workshop) is int):
        print.prettyerror("server.workshop must be an int!")
        raise SystemExit

    clear()

else:
    workshop = ""

    clear()

"""
    start.bat creating process.
"""
try:
    print.prettywait("Creating \"start.bat\"... [1/4]")

    create_start_bat = open("start.bat", "x")
    time.sleep(0.2) 

    print.prettysuccess("\"start.bat\" saved! [2/4]")

except FileExistsError:
    print.prettyerror("\"start.bat\" already exists!")
    raise SystemExit

try:
    print.prettywait("Writing all configurations into \"start.bat\"... [3/4]")

    port        = port
    tickrate    = tickrate
    lan         = lan
    max_players = max_players
    gamemode    = gamemode
    map         = map
    workshop    = workshop

    start_bat = open("start.bat", "a")
    start_bat.write(f"start \"SRCDS\" /B srcds.exe -game garrysmod -conlog -port {port} -console -conclearlog -condebug -tvdisable -maxplayers {max_players} +gamemode {gamemode} +map {map} +host_workshop_collection \"{workshop}\" -tickrate {tickrate} +fps_max {tickrate} +sv_lan {lan}\n:: Created via Garry's Mod Tools!")

    print.prettysuccess("\"start.bat\" successfully configured! [4/4]")
    raise SystemExit
except Exception as unknown_error:
    print.prettywarn("Whoops, unknown prettyerror!")
    # или пофикси сам
    # знаете, я и сам своего рода кодер
    print.prettywarn("Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    file_time = datetime.now().strftime("%H.%M.%S")

    try:
        create_error_log = open(f"prettyerror-{file_time}.log", "x")
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        error_log = open(f"prettyerror-{file_time}.log", "a")
        error_log.write(
        f"""Whoops! That's an prettyerror!
        \n--------------------------------------------------\n
        Type: {exc_type}\n
        File: {fname}\n
        Line: {exc_tb.tb_lineno}\n
        Detailed Error: {unknown_error}
        \n--------------------------------------------------\n
        OS: {sys.platform}\n
        CPU: {cpuinfo.get_cpu_info()['brand']}\n
        Python: {platform.python_version}
        """)

        raise SystemExit
    except FileExistsError:
        print.prettyerror(f"\"prettyerror-{file_time}.log\" already exists!")

        raise SystemExit