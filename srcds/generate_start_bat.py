import os
import time
import pretty_print
import pretty_error

clear = lambda: os.system("cls")
clear()

"""
    Port.
"""
pretty_print.prettyinfo("Name: Port [*].")
pretty_print.prettyinfo("Description: The port the server will run on.")
pretty_print.prettyinfo("Arguments: integer (e.g. 27015)")

port = int(pretty_print.prettyinput("Value: "))

if (not type(port) is int):
    pretty_print.prettyerror("server.port must be an integer!")

    raise SystemExit

elif (port <= 0 or port == ""):
    pretty_print.prettyerror("server.port must be something, like an example!")

    raise SystemExit

clear()

"""
    Tickrate.
"""
pretty_print.prettyinfo("Name: Tick Rate [*].")
pretty_print.prettyinfo("Description: The tick rate the server will run. Higher the number, more demanding it is on the CPU. A performant tickrate is around 30. Max: 128.")
pretty_print.prettyinfo("Arguments: integer (e.g. 33)")

tickrate = int(pretty_print.prettyinput("Value: "))

if (not type(tickrate) is int):
    pretty_print.prettyerror("server.tickrate must be an integer!")

    raise SystemExit

elif (tickrate < 16 or tickrate > 128):
    pretty_print.prettyerror("server.tickrate can't be lower than 16 or higher than 128!")

    raise SystemExit

clear()

"""
    LAN Server -> sv_lan 0/1.
"""
pretty_print.prettyinfo("Name: LAN Server [*].")
pretty_print.prettyinfo("Description: LAN servers only allow users from your local network to connect. Public servers will require you to port forward your server's port number.")
pretty_print.prettyinfo("Arguments: integer (e.g. 0)")

lan = int(pretty_print.prettyinput("Value: "))

if (not type(lan) is int):
    pretty_print.prettyerror("server.lan must be an integer!")

    raise SystemExit

elif (lan < 0 or lan > 1):
    pretty_print.prettyerror("server.lan can't be lower than 0 or higher than 1!")

    raise SystemExit

elif (lan == 1):
    pretty_print.prettywarn("server.lan = 1, it may not appear in your server browser!")
    pretty_print.prettyinfo("Press [ENTER] to continue generation.")

    input("")

clear()

"""
    Max Players.
"""
pretty_print.prettyinfo("Name: Max Players [*].")
pretty_print.prettyinfo("Description: The max amount of players that can play on this ")
pretty_print.prettyinfo("Arguments: integer (e.g. 128)")

max_players = int(pretty_print.prettyinput("Value: "))

if (not type(max_players) is int):
    pretty_print.prettyerror("server.max_players must be an integer!")

    raise SystemExit

elif (max_players <= 0 or max_players > 128):
    pretty_print.prettyerror("server.max_players can't be lower than 1 or higher than 128!")

    raise SystemExit

clear()

"""
    Gamemode.
"""
pretty_print.prettyinfo("Name: Gamemode [*].")
pretty_print.prettyinfo("Description: The name of your gamemode's folder.")
pretty_print.prettyinfo("Arguments: string (e.g. sandbox)")

gamemode = str(pretty_print.prettyinput("Value: "))

if (not type(gamemode) is str):
    pretty_print.prettyerror("server.gamemode must be an string!")

    raise SystemExit

elif (gamemode == ""):
    pretty_print.prettyerror("server.gamemode can't be blank!")

    raise SystemExit

clear()

"""
    Map.
"""
pretty_print.prettyinfo("Name: Map [*].")
pretty_print.prettyinfo("Description: The name of the map the server will run, must be included in your server files.")
pretty_print.prettyinfo("Arguments: string (e.g. gm_construct)")

map = str(pretty_print.prettyinput("Value: "))

if (not type(map) is str):
    pretty_print.prettyerror("server.map must be an string!")

    raise SystemExit

elif (map == ""):
    pretty_print.prettyerror("server.map can't be blank!")

    raise SystemExit

clear()

"""
    Workshop Collection ID.
"""
pretty_print.prettyinfo("Name: Workshop Collection ID - skip.")
pretty_print.prettyinfo("Description: It will skip adding of \"Workshop Collection ID\".")
pretty_print.prettyinfo("Arguments: string")

workshop_add = str(pretty_print.prettyinput("Add (Y/N): "))

if (workshop_add == "Y"):
    pretty_print.prettyinfo("Name: Workshop Collection ID - add.")
    pretty_print.prettyinfo("Description: The ID your steam workshop collection. This will be the addons the server automatically downloads. (Clients will not download these files)")
    pretty_print.prettyinfo("Arguments: integer (e.g. 2594826718)")

    workshop = int(pretty_print.prettyinput("Value: "))

    if (not type(workshop) is int):
        pretty_print.prettyerror("server.workshop must be an int!")
        raise SystemExit

    clear()

else:
    workshop = ""

    clear()

"""
    start.bat creating process.
"""
try:
    pretty_print.prettywait("Creating \"start.bat\"... [1/4]")

    create_start_bat = open("start.bat", "x")
    time.sleep(0.2) 

    pretty_print.prettysuccess("\"start.bat\" saved! [2/4]")
except FileExistsError:
    pretty_print.prettyerror("\"start.bat\" already exists!")
    raise SystemExit

try:
    pretty_print.prettywait("Writing all configurations into \"start.bat\"... [3/4]")

    start_bat = open("start.bat", "a")
    start_bat.write(f"start \"SRCDS\" /B srcds.exe -game garrysmod -conlog -port {port} -console -conclearlog -condebug -tvdisable -maxplayers {max_players} +gamemode {gamemode} +map {map} +host_workshop_collection \"{workshop}\" -tickrate {tickrate} +fps_max {tickrate} +sv_lan {lan}\n:: Created via Garry's Mod Tools!")

    pretty_print.prettysuccess("\"start.bat\" successfully configured! [4/4]")
    raise SystemExit
except Exception as unknown_error:
    pretty_print.prettywarn("Whoops, that's an unknown error for us!")
    # или пофикси сам
    # знаете, я и сам своего рода кодер
    pretty_print.prettywarn("Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    pretty_error.prettyerror(unknown_error)