import sys
from cx_Freeze import setup, Executable

options = {
"includes": ["os","re","sqlite3","PyQt5"], 

"include_files": ["Ui_database.py","Ui_input.py","data.db"]
}

target = Executable(
        script="Main.py",
        base="Win32GUI",
        icon="icon.ico"
)

setup(
        name="setup",
        version="1.0",
        description="the description",
    author="DuHua",
    options={"build_exe": options},
    executables=[target]
)