function New-Configuration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline)] 
        [string]$Name,

        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter()]
        [string]$Version = "1.0.0",

        [Parameter()]
        [ValidateSet("Linux", "Windows")]
        [string]$OpSys = "Windows"
    )

    begin {
        # begin is for example made for making connections to a db
        Write-Verbose "Beginning"
        $CounterPassed = 0 
        $CounterFailed = 0
    }
    
    # EVERYTHING THAT USES THE PIPE MUST GO IN PROCESS
    process {
        # algorithms must be inside process for example processing something for db
        try {
            # 1. Ensure the directory exists
            if (-not (Test-Path -Path $Path)) { 
                New-Item -ItemType Directory -Path $Path -Force | Out-Null
            }

            $FullFilePath = Join-Path -Path $Path -ChildPath "$Name.cfg" 
        
            Write-Host "Creating config for $Name (v$Version) at: $FullFilePath" -ForegroundColor Cyan
        
            # 2. write 
            $Version | Set-Content -Path $FullFilePath -Force
            $CounterPassed ++
        }
        catch {
            Write-Output $_.Exception.Message
            $CounterFailed ++
        }
    }

    end {
        # end is for example closing db connections
        Write-Verbose "Ending"
        Write-Verbose "$CounterFailed - failed, $CounterPassed - passed"
    }
}

$configPath = Read-Host "Enter the config path"

# This works for a single call
New-Configuration -Name "Python" -Version "1.0.1" -Path $configPath -OpSys "Windows" # works once

# works too 
$names = @("Testconfig1", "Testconfig4")
$names | New-Configuration -Path $configPath -Verbose