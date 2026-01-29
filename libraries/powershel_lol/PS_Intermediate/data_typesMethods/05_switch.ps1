$newItem = ".ext"

switch -Wildcard ($newItem) {
    ".ext" { "Goot" }
    ".*" { "Yes" }
    "*t" { "No" }
    Default { "Bad" }
}

$fileName = "backup_2024_01_01.zip"

switch -Wildcard ($fileName) {
    "backup*" { "This is a backup file" }
    "*.zip" { "This is a compressed archive" }
    "*[0-9]*" { "This filename contains numbers" }
}

$proccesedList = [System.Collections.Generic.List[PSCustomObject]]::new()

Get-Process | ForEach-Object {
    $CurrentName = $_.Name
    $Category = "" 

    switch -Wildcard ($CurrentName) {
        "chrome" { $Category = "App" }
        "*host*" { $Category = "System" }
        Default { $Category = "UNKNOWN" }
    }

    $obj = [PSCustomObject]@{
        Process_name = $CurrentName
        Category     = $Category
    }

    $proccesedList.Add($obj)
}

$proccesedList | Where-Object Category -eq "System"