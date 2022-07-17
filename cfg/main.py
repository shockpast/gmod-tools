import os
import time

import modules.pretty_print as pretty_print
import modules.pretty_error as pretty_error

clear = lambda: os.system("cls")
clear()

"""
"""
hostname = pretty_print.askinput(
    "Server Name.",
    "The name of the server that will be displayed in the Server Browser.",
    "any (e.g. t.me/shockpast)")
password = pretty_print.askinput(
    "Password.",
    "The password of the server. Used to create private servers. (Leave blank to setup a public server)",
    "any (e.g. qwerty123456)")
download_url = pretty_print.askinput(
    "Download URL",
    "If you want new players to download the custom server's files (music, miscs, maps, etc.) from a remote server, type its root address here.",
    "any (e.g. https://myserver.com/fastdl/)")
loading_url = pretty_print.askinput(
    "Loading URL",
    "If not empty, the given URL will display the webpage that is associated with to the user while loading.",
    "any (e.g. https://myserver.com/cool_loading_url/)")
netsize = int(pretty_print.askinput(
    "Maximum File Size for Net",
    "Maximum allowed file size for uploading in MB.",
    "integer (e.g. 64)"))

"""
    Sandbox Settings.
"""
noclip = int(pretty_print.askinput(
    "NoClip",
    "Enable/Disable NoClip for everyone.",
    "integer (e.g. 1)"))
godmode = int(pretty_print.askinput(
    "God Mode",
    "Enable/Disable God Mode for everyone.",
    "integer (e.g. 1)"))
php = int(pretty_print.askinput(
    "Players Hurt Players",
    "Enable/Disable damage that being applied to players (from players).",
    "integer (e.g. 1)"))

"""
    Description is long...
"""
props = int(pretty_print.askinput(
    "Maximum Props",
    "The maximum amount of props a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned props will disappear.",
    "integer (e.g. 150)"))
ragdolls = int(pretty_print.askinput(
    "Maximum Ragdolls",
    "The maximum amount of ragdolls a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned ragdolls will disappear.",
    "integer (e.g. 60)"))
npcs = int(pretty_print.askinput(
    "Maximum NPCs",
    "The maximum amount of NPCs (Non-Playable Characters) a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned NPCs will disappear.",
    "integer (e.g. 20)"))
ballons = int(pretty_print.askinput(
    "Maximum Ballons",
    "The maximum amount of balloons a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned balloons will disappear.",
    "integer (e.g. 10)"))
effects = int(pretty_print.askinput(
    "Maximum Effects",
    "The maximum amount of effects a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned effects will disappear.",
    "integer (e.g. 10)"))
dynamite = int(pretty_print.askinput(
    "Maximum Dynamite",
    "The maximum amount of dynamites a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned dynamites will disappear.",
    "integer (e.g. 5)"))
lamps = int(pretty_print.askinput(
    "Maximum Lamps",
    "The maximum amount of lamps a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned lamps will disappear.",
    "integer (e.g. 10)"))
thrusters = int(pretty_print.askinput(
    "Maximum Thrusters",
    "The maximum amount of thrusters a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned thrusters will disappear.",
    "integer (e.g. 5)"))
wheels = int(pretty_print.askinput(
    "Maximum Wheels",
    "The maximum amount of wheels a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned wheels will disappear.",
    "integer (e.g. 10)"))
hoverballs = int(pretty_print.askinput(
    "Maximum Hoverballs",
    "The maximum amount of hoverballs a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned hoverballs will disappear.",
    "integer (e.g. 10)"))
vehicles = int(pretty_print.askinput(
    "Maximum Vehicles",
    "The maximum amount of vehicles a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned vehicles will disappear.",
    "integer (e.g. 0)"))
buttons = int(pretty_print.askinput(
    "Maximum Buttons",
    "The maximum amount of buttons a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned buttons will disappear.",
    "integer (e.g. 5)"))
emitters = int(pretty_print.askinput(
    "Maximum Emitters",
    "The maximum amount of emitters a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned emitters will disappear.",
    "integer (e.g. 0)"))

"""
"""
lan = int(pretty_print.askinput(
    "LAN Server",
    "If enabled, the server will only be visible on the Local Area Network.",
    "integer (e.g. 0)"))
alltalk = int(pretty_print.askinput(
    "All Talk",
    "Enable/disable letting both teams voice chat with each other.",
    "integer (e.g. 0)"))
cheats = int(pretty_print.askinput(
    "Cheats",
    "NOT RECOMMENDED! After enabling cheating, achievements cannot be earned.",
    "integer (e.g. 0)"))

"""
    End.
"""
try:
    open("server.cfg", "x")

    try:
        with open("server.cfg", "a") as file:
            file.write(f"""
hostname \"{hostname}\"
sv_password \"{password}\"

sv_region 255

log on
sv_logbans 1
sv_logecho 1
sv_logfile 1
sv_log_onefile 1

sv_downloadurl \"{download_url}\"
sv_loadingurl \"{loading_url}\"

net_maxfilesize {netsize}

sv_lan {lan}
sv_alltalk {alltalk}
sv_cheats {cheats}
sv_allowcslua 0
sv_pausable 0
sv_allowupload 0
sv_allowdownload 0

sbox_noclip {noclip}
sbox_godmode {godmode}
sbox_weapons 0
sbox_playershurtplayers {php}
sbox_maxprops {props}
sbox_maxragdolls {ragdolls}
sbox_maxnpcs {npcs}
sbox_maxballoons {ballons}
sbox_maxeffects {effects}
sbox_maxdynamite {dynamite}
sbox_maxlamps {lamps}
sbox_maxthrusters {thrusters}
sbox_maxwheels {wheels}
sbox_maxhoverballs {hoverballs}
sbox_maxvehicles {vehicles}
sbox_maxbuttons {buttons}
sbox_maxemitters {emitters}
        """)
    except FileExistsError as fileError:
        pretty_print.prettywarn(fileError)

    raise SystemExit
except Exception as unknown_error:
    pretty_print.prettywarn("Whoops, that's an unknown error for us!")
    pretty_print.prettywarn("Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    pretty_error.prettyerror(unknown_error)