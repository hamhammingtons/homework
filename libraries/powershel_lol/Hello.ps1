# # commands = commandlets
# Get-Alias 
# Get-Date #  FORMAT FOR COMMANDLETS: verb - noun ->== comandlet 
# Get-Command -noun Service # search by noun if you dont know the name
# Get-Help Get-Service # you can do -full to get eveyrthing 
# Get-Service GoogleChromeElevationService
# Set-Location -Path C:\[location] very useful. NOTE: make sure to use quotes if your file path has [, " ", any type of special char]
# .\[what to execute (file in your folder)]
# " " is a space btw

Write-Host "hello"
get-executionpolicy # if not RemoteSigned = you can do: set-executionpolicy -ExecutionPolicy RemoteSigned