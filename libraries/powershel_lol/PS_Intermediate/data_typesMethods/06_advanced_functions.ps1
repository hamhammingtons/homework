function Get-ProcessHealth {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [ValidateSet("chrome", "explorer", "svchost")]
        [string]$ProcessName
    )
    
    begin {
        Write-Debug "__Init__ list"
        $ReportList = [System.Collections.Generic.List[PSCustomObject]]::new()
    }
    
    process {
        Write-Verbose "checking: $ProcessName"
        $foundProcesses = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue # returns a list 

        if ($null -eq $foundProcesses) {
            Write-Debug "Process '$ProcessName' is not currently running"
        }
        else {
            foreach ($proc in $foundProcesses) {
                $newobj = [PSCustomObject]@{
                    Name         = $proc.Name
                    ID           = $proc.Id
                    IsActive     = $true
                    VM_Megabytes = [math]::Round($proc.WorkingSet / 1MB, 2)
                }
                $ReportList.Add($newobj)
            }
        }
    }
    
    end {
        Write-Debug "Sending Report to output"
        $ReportList
    }
}

Get-ProcessHealth "chrome" 