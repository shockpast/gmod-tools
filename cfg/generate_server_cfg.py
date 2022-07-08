import os
import time
import modules.pretty_print as pretty_print
import modules.pretty_error as pretty_error

clear = lambda: os.system("cls")
clear()

"""
    Basic settings.
"""
# hostname.
pretty_print.prettyinfo("Name: hostname [1/38]")
pretty_print.prettyinfo("Description: The name of the server that will be displayed in the Server Browser.")
pretty_print.prettyinfo("Arguments: any (e.g. Garry's Mod)")

hostname = pretty_print.prettyinput("Value: ")

if (hostname == ""):
    pretty_print.prettyerror("cfg.hostname must be something, like an example!")

    raise SystemExit

clear()

# sv_password
pretty_print.prettyinfo("Name: sv_password [2/38]")
pretty_print.prettyinfo("Description: The password of the server. Used to create private servers. (Leave blank to setup a public server)")
pretty_print.prettyinfo("Arguments: any (e.g. qwerty1234)")

sv_password = pretty_print.prettyinput("Value: ")

clear()

"""
    RCON (Remote CONtrol) settings 
"""
# rcon_password
pretty_print.prettyinfo("Name: rcon_password [3/38]")
pretty_print.prettyinfo("Description: The RCON password of the server that will allow admins to send commands to the server using Console Variables via Garry's Mod's console. Only you (the owner) should know this password!")
pretty_print.prettyinfo("Arguments: any (e.g. Garry's Mod)")

rcon_password = pretty_print.prettyinput("Value: ")

if (not rcon_password == ""):
    pretty_print.prettywarn("cfg.rcon_password can be stolen through backdoors, use it with risk.")
    pretty_print.prettyinfo("Press [ENTER] to continue generation.")
    input("")

clear()

# sv_rcon_log
pretty_print.prettyinfo("Name: sv_rcon_log [4/38]")
pretty_print.prettyinfo("Description: RCON logging. If enabled, the RCON information will be kept")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

try:
    sv_rcon_log = int(pretty_print.prettyinput("Value: "))
except ValueError:
    sv_rcon_log = 0
    pass

clear()

"""
    Network settings
"""
# sv_downloadurl
pretty_print.prettyinfo("Name: sv_downloadurl [5/38]")
pretty_print.prettyinfo("Description: If not empty, the given URL will download files for the client (FastDL)")
pretty_print.prettyinfo("Arguments: any")

sv_downloadurl = pretty_print.prettyinput("Value: ")

clear()

# sv_loadingurl
pretty_print.prettyinfo("Name: sv_loadingurl [6/38]")
pretty_print.prettyinfo("Description: If not empty, the given URL will display the webpage that is associated with to the user while loading")
pretty_print.prettyinfo("Arguments: any")

sv_loadingurl = pretty_print.prettyinput("Value: ")

clear()

# sv_allowupload
pretty_print.prettyinfo("Name: sv_allowupload [7/38]")
pretty_print.prettyinfo("Description: Enable/disable clients to upload customizations files")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sv_allowupload = int(pretty_print.prettyinput("Value: "))

clear()

# sv_allowdownload
pretty_print.prettyinfo("Name: sv_allowdownload [8/38]")
pretty_print.prettyinfo("Description: Enable/disable ability for clients to download missing files")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sv_allowdownload = int(pretty_print.prettyinput("Value: "))

clear()

# net_maxfilesize
pretty_print.prettyinfo("Name: net_maxfilesize [9/38]")
pretty_print.prettyinfo("Description: Maximum allowed file size for uploading in MB")
pretty_print.prettyinfo("Arguments: int (e.g. 15)")

net_maxfilesize = int(pretty_print.prettyinput("Value: "))

clear()

"""
    Sandbox Settings.
"""
# physgun_limited
pretty_print.prettyinfo("Name: physgun_limited [10/38]")
pretty_print.prettyinfo("Description: Limiting player's physgun")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

physgun_limited = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_noclip
pretty_print.prettyinfo("Name: sbox_noclip [11/38]")
pretty_print.prettyinfo("Description: Enable/disable NoClip")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sbox_noclip = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_godmode
pretty_print.prettyinfo("Name: sbox_godmode [12/38]")
pretty_print.prettyinfo("Description: Enable/disable God Mode")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sbox_godmode = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_playershurtplayers
pretty_print.prettyinfo("Name: sbox_playershurtplayers [13/38]")
pretty_print.prettyinfo("Description: Enable/disable PvP (Player vs. Player)")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sbox_playershurtplayers = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxprops
pretty_print.prettyinfo("Name: sbox_maxprops [14/38]")
pretty_print.prettyinfo("Description: The maximum amount of props a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned props will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 150)")

sbox_maxprops = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxragdolls
pretty_print.prettyinfo("Name: sbox_maxragdolls [15/38]")
pretty_print.prettyinfo("Description: The maximum amount of ragdolls a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned ragdolls will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxragdolls = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxnpcs
pretty_print.prettyinfo("Name: sbox_maxragdolls [16/38]")
pretty_print.prettyinfo("Description: The maximum amount of NPCs (Non-Playable Characters) a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned NPCs will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxnpcs = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxballoons
pretty_print.prettyinfo("Name: sbox_maxballoons [17/38]")
pretty_print.prettyinfo("Description: The maximum amount of balloons a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned balloons will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxballoons = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxeffects
pretty_print.prettyinfo("Name: sbox_maxeffects [18/38]")
pretty_print.prettyinfo("Description: The maximum amount of effects a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned effects will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxeffects = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxdynamite
pretty_print.prettyinfo("Name: sbox_maxdynamite [19/38]")
pretty_print.prettyinfo("Description: The maximum amount of dynamites a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned dynamites will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxdynamite = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxlamps
pretty_print.prettyinfo("Name: sbox_maxlamps [20/38]")
pretty_print.prettyinfo("Description: The maximum amount of lamps a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned lamps will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxlamps = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxthrusters
pretty_print.prettyinfo("Name: sbox_maxthrusters [21/38]")
pretty_print.prettyinfo("Description: The maximum amount of thrusters a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned thrusters will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxthrusters = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxwheels
pretty_print.prettyinfo("Name: sbox_maxwheels [22/38]")
pretty_print.prettyinfo("Description: The maximum amount of wheels a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned wheels will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxwheels = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxlights
pretty_print.prettyinfo("Name: sbox_maxlights [23/38]")
pretty_print.prettyinfo("Description: The maximum amount of lights a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned wheels will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxlights = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxcameras
pretty_print.prettyinfo("Name: sbox_maxcameras [24/38]")
pretty_print.prettyinfo("Description: The maximum amount of cameras a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned wheels will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxcameras = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxsents
pretty_print.prettyinfo("Name: sbox_maxsents [25/38]")
pretty_print.prettyinfo("Description: The maximum amount of scripted entities a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned wheels will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxsents = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxhoverballs
pretty_print.prettyinfo("Name: sbox_maxhoverballs [26/38]")
pretty_print.prettyinfo("Description: The maximum amount of hover-balls a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned hover-balls will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxhoverballs = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxvehicles
pretty_print.prettyinfo("Name: sbox_maxvehicles [27/38]")
pretty_print.prettyinfo("Description: The maximum amount of vehicles a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned vehicles will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxvehicles = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxbuttons
pretty_print.prettyinfo("Name: sbox_maxbuttons [28/38]")
pretty_print.prettyinfo("Description: The maximum amount of buttons a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned buttons will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxbuttons = int(pretty_print.prettyinput("Value: "))

clear()

# sbox_maxemitters
pretty_print.prettyinfo("Name: sbox_maxemitters [29/38]")
pretty_print.prettyinfo("Description: The maximum amount of emitters a player will be able to spawn. If a player keeps spawning after this limit, previously-spawned emitters will disappear")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

sbox_maxemitters = int(pretty_print.prettyinput("Value: "))

clear()

"""
    General settings
"""
# sv_lan
pretty_print.prettyinfo("Name: sv_lan [30/38]")
pretty_print.prettyinfo("Description: If enabled, the server will only be visible on the Local Area Network")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sv_lan = int(pretty_print.prettyinput("Value: "))

clear()

# sv_alltalk
pretty_print.prettyinfo("Name: sv_alltalk [31/38]")
pretty_print.prettyinfo("Description: Enable/disable letting both teams voice chat with each other")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

sv_alltalk = int(pretty_print.prettyinput("Value: "))

clear()

""" # mp_friendlyfire
pretty_print.prettyinfo("Name: mp_friendlyfire")
pretty_print.prettyinfo("Description: Enable/disable \"Friendly fire\". (Teammates can kill each other)")
pretty_print.prettyinfo("Arguments: int (e.g. 30)")

mp_friendlyfire = int(pretty_print.prettyinput("Value: "))

clear() """

# sv_cheats
pretty_print.prettyinfo("Name: sv_cheats [32/38]")
pretty_print.prettyinfo("Description: NOT RECOMMENDED! After enabling cheating, achievements cannot be earned")
pretty_print.prettyinfo("Arguments: int (e.g. 0)")

sv_cheats = int(pretty_print.prettyinput("Value: "))

clear()

# sv_allowcslua
pretty_print.prettyinfo("Name: sv_allowcslua [33/38]")
pretty_print.prettyinfo("Description: NOT RECOMMENDED! Allows client(s) to execute any LUA file (only client)")
pretty_print.prettyinfo("Arguments: int (e.g. 0)")

sv_allowcslua = int(pretty_print.prettyinput("Value: "))

clear()

# sv_pausable
pretty_print.prettyinfo("Name: sv_pausable [34/38]")
pretty_print.prettyinfo("Description: NOT RECOMMENDED! Enable/disable the ability to pause the server. Works only if \"sv_cheats\" is set to 1")
pretty_print.prettyinfo("Arguments: int (e.g. 0)")

sv_pausable = int(pretty_print.prettyinput("Value: "))

clear()

""" # mp_forcecamera
pretty_print.prettyinfo("Name: mp_forcecamera")
pretty_print.prettyinfo("Description: Forces Spectator Mode's camera for dead players")
pretty_print.prettyinfo("Arguments: int (e.g. 0)")

mp_forcecamera = int(pretty_print.prettyinput("Value: "))

clear() """

"""
    Idle settings
"""
# mp_disable_autokick
pretty_print.prettyinfo("Name: mp_disable_autokick [35/38]")
pretty_print.prettyinfo("Description: Enable/disable auto kick for idling")
pretty_print.prettyinfo("Arguments: int (e.g. 0)")

mp_disable_autokick = int(pretty_print.prettyinput("Value: "))

clear()

"""
    Technical settings
"""
# mp_falldamage
pretty_print.prettyinfo("Name: mp_falldamage [36/38]")
pretty_print.prettyinfo("Description: Amount of damage players sustains from a fall")
pretty_print.prettyinfo("Arguments: int (e.g. 1)")

mp_falldamage = int(pretty_print.prettyinput("Value: "))

clear()

"""
    Other
"""
# sv_location
pretty_print.prettyinfo("Name: sv_location [37/38]")
pretty_print.prettyinfo("Description: The server will be displayed in the Server Browser with selected flag (such as RU)")
pretty_print.prettyinfo("Arguments: int (e.g. ru)")

sv_location = pretty_print.prettyinput("Value: ")

clear()

# sv_region
pretty_print.prettyinfo("Name: sv_region [38/38]")
pretty_print.prettyinfo("Description: The server will be displayed in the Server Browser for the selected region")
pretty_print.prettyinfo("Arguments: int (e.g. 255)")

sv_region = int(pretty_print.prettyinput("Value: "))

clear()

"""
    Trying to create "server.cfg"...
"""
try:
    pretty_print.prettywait("Creating \"server.cfg\"... [1/4]")

    create_server_cfg = open("server.cfg", "x")
    time.sleep(0.2) 

    pretty_print.prettysuccess("\"server.cfg\" saved! [2/4]")
except FileExistsError:
    pretty_print.prettyerror("\"server.cfg\" already exists!")
    raise SystemExit

"""
    Trying to write into "server.cfg"...
"""
try:
    pretty_print.prettywait("Writing all configurations into \"server.cfg\"... [3/4]")

    server_cfg = open("server.cfg", "a")
    server_cfg.write(f"""# Created via Garry's Mod Tools!

# General. 
hostname \"{hostname}\"
rcon_password \"{rcon_password}\"
sv_password \"{sv_password}\"
sv_downloadurl \"{sv_downloadurl}\"
sv_loadingurl {sv_loadingurl}
sv_allowupload {sv_allowupload}
sv_allowdownload {sv_allowdownload}
sv_allowcslua {sv_allowcslua}
sv_cheats {sv_cheats}
sv_hibernate_think 0
sv_location \"{sv_location}\"
sv_region {sv_region}

# Sandbox.
physgun_limited {physgun_limited}
sbox_weapons 0
sbox_godmode {sbox_godmode}
sbox_playershurtplayers {sbox_playershurtplayers}
sbox_maxprops {sbox_maxprops}
sbox_maxragdolls {sbox_maxragdolls}
sbox_maxvehicles {sbox_maxvehicles}
sbox_maxeffects {sbox_maxeffects}
sbox_maxballoons {sbox_maxballoons}
sbox_maxcameras {sbox_maxcameras}
sbox_maxnpcs {sbox_maxnpcs}
sbox_maxsents {sbox_maxsents}
sbox_maxdynamite {sbox_maxdynamite}
sbox_maxlamps {sbox_maxlamps}
sbox_maxlights {sbox_maxlights}
sbox_maxwheels {sbox_maxwheels}
sbox_maxthrusters {sbox_maxthrusters}
sbox_maxhoverballs {sbox_maxhoverballs}
sbox_maxbuttons {sbox_maxbuttons}
sbox_maxemitters {sbox_maxemitters}
gmod_maxammo 9999
gmod_suit 0
sbox_noclip {sbox_noclip}
sbox_bonemanip_npc 0
sbox_bonemanip_player 0
sbox_bonemanip_misc 0
mp_falldamage {mp_falldamage}""")

    pretty_print.prettysuccess("\"server.cfg\" successfully configured! [4/4]")
    raise SystemExit
except Exception as unknown_error:
    pretty_print.prettywarn("Whoops, that's an unknown error for us!")
    # или пофикси сам
    # знаете, я и сам своего рода кодер
    pretty_print.prettywarn("Contact with us: https://github.com/shockpast/gmod-tools/issues/new")

    pretty_error.prettyerror(unknown_error)