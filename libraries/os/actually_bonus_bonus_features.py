import os

print(
    os.name
)  # nt - windows, posix - unix like (ex. linux), java,ce,os2,ricos - very rare and not used often

os.startfile(
    r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2510.14.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe"
)  # opens a file based on path i think

system_folder = os.environ.get("SystemRoot")
notepad_path = os.path.join(
    system_folder, "System32", "notepad.exe"  # type: ignore
)  # type: ignore # same thing but with join, which is safer

# This is much safer than the WindowsApps path!
os.startfile(notepad_path)


"""btw, path is a sub-module which has a lot of methods, but i dont really want to use it right now because of some things"""
