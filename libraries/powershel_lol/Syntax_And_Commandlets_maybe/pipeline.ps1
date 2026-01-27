Get-Service -Name Spooler # whats running on your pc [can specify name], you can also pass a string variable as a -Name

# Start-Service -Name Spooler

Get-Service -Name Spooler | Stop-Service # catches the service -> returns service controller -> stop-service catches it

"Spooler" | Get-Service # we can also just specify a string and then its passed thru get-service

"Spooler" | Get-Service | Start-Service
# so like a hierarchial structure we start from the left to the right. 
# so spooler goes first, passes itself to get-service, then it converts it to service controller to start-service 

$arraArray = New-Object -TypeName System.Collections.ArrayList
$arraArray.AddRange(@("Spooler", "w32time"))

$arraArray | Get-Service # does like a for loop thru its items, if its legit then does get-service output- cool


$arraArray | Get-Service | ForEach-Object{Write-Output "Service: $($_.displayname) $($_.status)"}

# wow thats cool ^^^ so when youre doing like an f string in powershell you can just do $(something) and it will work like f"{}"
# its called "Subexpression" ^^^

# also my theory is that get-service returns like an object and then we can mention its properties (kinda like unpacking)
# ^^^ true 

Get-Service | Where-Object {$_.Status -eq "Running"} | ForEach-Object {$_.DisplayName}

########### IN DEPTH ##############

# basically when youre working in python you have a variable which will be the iteration variable.
# but whenever were using ForEach-Object (which is almost exactly the same as for loop in python
# we dont get to choose the name 

# So a thing called "placeholder" holds the object which is an iterable variable 
# it is a "$_"
    
# its used a lot in programs for fixing stuff 
# for example i want to capitalize each letter in a list 

$myBadarray = New-Object -TypeName System.Collections.ArrayList
$myBadarray.AddRange(@("hello", "world"))
$myBadarray | ForEach-Object {$_.ToUpper()}