$Profile = [ordered]@{ # this fixes the problem with hash tables being random
    Name = "Bob"
    Age  = 25
    City = "Undefined"
}

foreach ($item in $Profile.GetEnumerator()) {
    # so here it is like dict.items() but here we do .GetEnumerator()
    Write-Host "The key $($item.Key), $($item.Value) value"
}

# Splatting 

$neededTopass = @{
    Path        = "C:\test.txt"
    Destination = "D:\backup.txt"
    Force       = $true
    Recurse     = $true
    Verbose     = $true
}

# Copy-Item @neededTopass -- if we already assign the keys they will be passed into copy-item correctly if theyre 
# correctly set up (the keys should be actual parameters in a commandlet)