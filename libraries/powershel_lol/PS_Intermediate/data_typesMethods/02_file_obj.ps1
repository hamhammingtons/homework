# --- THE FILE OBJECT LAB ---

# 1. How to "Capture" a File Object
# Get-Item is for one specific thing. Get-ChildItem is for lists.
$file = Get-Item -Path "C:\Users\Admin\OneDrive\Рабочий стол\Задания Excel_мини проект.xlsx"

# 2. Properties (The "Metadata" or "Adjectives")
$file.Name           # "script.ps1"
$file.Extension      # ".ps1"
$file.BaseName       # "script" (The name WITHOUT the extension - VERY useful!)
$file.FullName       # The complete path "C:\Users\..."
$file.Length         # File size in BYTES
$file.LastWriteTime  # Date and time it was last saved
$file.Attributes     # Shows if it's Hidden, ReadOnly, or an Archive

# 3. Directory Properties
# The file object even knows about the folder it lives in
$file.DirectoryName  # The path to the parent folder 
$file.Directory      # This is actually ANOTHER object (a Folder Object!) Basically a parent object.

# 4. Methods (The "Verbs")
# These are actions the file can perform on itself
# $file.Delete()
# $file.CopyTo("C:\Backup\script.ps1")
# $file.MoveTo("C:\NewFolder\script.ps1")
# $file.Rename("new_name.ps1") # Note: In newer PS, we usually use Rename-Item