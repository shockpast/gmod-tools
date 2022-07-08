from datetime import datetime

import sys
import platform
import cpuinfo
import os

import modules.pretty_print as pretty_print

def prettyerror(error):
    file_time = datetime.now().strftime("%H.%M.%S")

    try:
        _ = open(f"error-{file_time}.log", "x")
        
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        error_log = open(f"error-{file_time}.log", "a")
        error_log.write(
        f"""--------------------------------------------------\n
    Type: "{exc_type}"\n
    File: "{fname}"\n
    Line: "{exc_tb.tb_lineno}"
        \n--------------------------------------------------\n
    Detailed Log: {error}
        \n--------------------------------------------------\n
    OS: "{platform.platform()}"\n
    CPU: "{cpuinfo.get_cpu_info()["brand_raw"]}"\n
    Python: "{platform.python_version()}"
        \n--------------------------------------------------""")

        raise SystemExit
    except FileExistsError:
        pretty_print.prettyerror(f"\"error-{file_time}.log\" already exists!")

        raise SystemExit