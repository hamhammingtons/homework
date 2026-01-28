#$files = Get-ChildItem -Path $desktopPath
#$files.Name  # PowerShell "unrolls" the array and gives you the names automatically

$report = Get-ChildItem -Path _ -Filter *.lnk | ForEach-Object {
    [PSCustomObject]@{
        Name    = $_.Name
        Target  = $_.FullName
        Size_kb = [System.Math]::Round($_.Length / 1kb, 2) 
    }
}

# THEN report automatically becomes a pscustomobject with the things you wanted 


$exeFiles = Get-ChildItem -Path C:\Windows -Filter "*.exe" | ForEach-Object {
    $withoutExe = $_.BaseName 
    $IsRunningProperty = Get-Process $withoutExe -ErrorAction SilentlyContinue # remember this is very useful
    if (-not $IsRunningProperty) {
        $IsRunningProperty = "Not Running"
    }
    else {
        $IsRunningProperty = "running"	
    }
    [PSCustomObject]@{
        Name    = $_.Name
        Running = $IsRunningProperty
    }
}
$exeFiles | Sort-Object -Descending 