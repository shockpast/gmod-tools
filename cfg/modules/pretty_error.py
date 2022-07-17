from datetime import datetime

import sys
import platform
import cpuinfo # is it pre-installed in python? idk
import os

def prettyerror(error):
    fileTime = datetime.now().strftime("%H.%M.%S")

    try:
        open(f"error_{fileTime}.log", "x")

        excType, _, excTb = sys.exc_info()
        fileName = os.path.split(excTb.tb_frame.f_code.co_filename)[1]

        errorLog = open(f"error-{fileTime}.log", "a")
        errorLog.write(
        f"""--------------------------------------------------\n
    Type: "{excType}"\n
    File: "{fileName}"\n
    Line: "{excTb.tb_lineno}"
        \n--------------------------------------------------\n
    Detailed Log: {error}
        \n--------------------------------------------------\n
    OS: "{platform.platform()}"\n
    CPU: "{cpuinfo.get_cpu_info()["brand_raw"]}"\n
    Python: "{platform.python_version()}"
        \n--------------------------------------------------""")

        raise SystemExit
    except FileExistsError:
        raise SystemExit