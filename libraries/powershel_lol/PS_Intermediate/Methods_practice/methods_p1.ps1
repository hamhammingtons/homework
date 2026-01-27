function New-Configuration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter()]
        [string]$Version = "1.0.0",

        [Parameter()]
        [ValidateSet("Linux", "Windows")]
        [string]$OpSys = "Windows"
    )
    
    # 1. Ensure the directory exists
    if (-not (Test-Path -Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
    
    # 2. Safely combine the path and filename
    $FullFilePath = Join-Path -Path $Path -ChildPath "$Name.cfg" #idk what this is
    
    Write-Host "Creating config for $Name (v$Version) at: $FullFilePath" -ForegroundColor Cyan
    
    # 3. Write content directly (this creates/overwrites the file in one go)
    $Version | Set-Content -Path $FullFilePath -Force
}

# Prompt user for config path
$configPath = Read-Host "Enter the config path"

# Execute
New-Configuration -Name "Python" -Version "1.0.1" -Path $configPath -OpSys "Windows" # will return an error if not linux or windows

$names = @("Testconfig1", "Testconfig4")

$names | New-Configuration -Path $configPath # doesnt work, it doesnt accept pipelines