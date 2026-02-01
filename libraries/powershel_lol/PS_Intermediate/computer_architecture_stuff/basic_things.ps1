# This shows how many "Committed" pages (Valid Bit likely 1) 
# versus "Reserved" pages (Valid Bit is 0) a process has.
Get-Process chrome | Select-Object Name, @{Name = "Committed_MB"; Expression = { $_.PagedMemorySize64 / 1MB } }, @{Name = "WorkingSet_MB"; Expression = { $_.WorkingSet64 / 1MB } }