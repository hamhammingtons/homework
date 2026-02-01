Get-Process | Select-Object Name, Id, VirtualMemorySize64, WorkingSet64 | Sort-Object WorkingSet64 -Descending | Select-Object -First 10
Get-Process | Select-Object Name, PageFaults | Sort-Object PageFaults -Descending | Select-Object -First 5

$mem = Get-Process | Measure-Object -Property VirtualMemorySize64, WorkingSet64 -Sum
Write-Host "The Illusion (Virtual): $([math]::round($mem.SumVirtualMemorySize64 / 1GB, 2)) GB"
Write-Host "The Reality (Physical): $([math]::round($mem.SumWorkingSet64 / 1GB, 2)) GB"