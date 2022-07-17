import os
import time

import modules.pretty_print as pretty_print
import modules.pretty_error as pretty_error

clear = lambda: os.system("cls")
clear()

"""
    Configuration.
"""
port = int(pretty_print.askinput(
    "Port [*]",
    "The port the server will run on.",
    "integer (e.g. 27015)"))
tickrate = int(pretty_print.askinput(
    "Tick Rate [*]",
    "The tick rate the server will run. Higher the number, more demanding it is on the CPU. A performant tickrate is around 30.",
    "integer (e.g. 66)"))
lan = int(pretty_print.askinput(
    "LAN Server [*]",
    "LAN servers only allow users from your local network to connect. Public servers will require you to port forward your server's port number.",
    "integer (e.g. 0)"))
max_players = int(pretty_print.askinput(
    "Max Players [*]",
    "The max amount of players that can play on this server.",
    "integer (e.g. 128)"))
gamemode = pretty_print.askinput(
    "Gamemode [*]",
    "The name of your gamemode's folder.",
    "any (e.g. sandbox)")
map = pretty_print.askinput(
    "Map [*]",
    "The name of the map the server will run, must be included in your server files.",
    "any (e.g. gm_construct)")

"""
    File Creation.
"""
try:
    open("start.bat", "x")

    try:
        with open("start.bat", "a") as file:
            file.write(f"start \"SRCDS\" /B srcds.exe -game garrysmod -conlog -port {port} -console -conclearlog -condebug -tvdisable -maxplayers {max_players} +gamemode {gamemode} +map {map} -tickrate {tickrate} +fps_max {tickrate} +sv_lan {lan}\n:: Created via Garry's Mod Tools!")
    except FileExistsError as fileError:
        pretty_print.prettywarn(fileError)

    raise SystemExit
except Exception as unknown_error:
    pretty_print.prettywarn("Whoops, that's an unknown error for us!")
    pretty_print.prettywarn("Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    pretty_error.prettyerror(unknown_error)