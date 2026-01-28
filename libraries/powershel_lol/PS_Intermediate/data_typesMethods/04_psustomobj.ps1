$desktopPath = [System.Environment]::GetFolderPath('Desktop')
$filePath = Join-Path -Path $desktopPath -ChildPath "Counter-Strike 1.6 RUS.lnk"

# 1. Get the file (This is fine to 'Stop' because the file MUST be there)
$file = Get-Item -Path $filePath -ErrorAction Stop

# 2. Check for the process (Use SilentlyContinue so it doesn't crash if the game is off)
$proc = Get-Process -Name "hl" -ErrorAction SilentlyContinue

# 3. Logic: Determine the status string
if ($null -eq $proc) {
    $status = "Not Running"
}
elseif ($proc.MainWindowHandle -eq 0) {
    $status = "Background"
}
else {
    $status = "Running"
}

# 4. Create the Object
$properties = [PSCustomObject]@{
    Name      = $file.Name
    Extension = $file.Extension
    Status    = $status
}

# Output the result
$properties