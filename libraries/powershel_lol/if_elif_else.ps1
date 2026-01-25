$a = 1 
$b = 2 

$a -eq $b # equals
$a -lt $b # less than
$a -le $b # less or equals to 

# and gt = greater than, ge - greater than or equals to

$a -ne $b  # not equals to 

@(1,2,3) -contains 2 # is like "if 2 in list"
@("test","test") -contains "TEST" #not case sensetive
# if we want it to make case sensetive 
@("bB", "fF") -ccontains "bb" # caseSensetive-contains 

#most of commands which have "c" in them- means case sensetive
# ex cc... or ceq...
'ceq' -ceq 'Ceq'

$filePath = "C:\Users\Admin\OneDrive\Рабочий стол\Python, tasks done by me\howework_for_itstep\libraries\powershel_lol\data.txt"

Test-Path -Path $filePath

if((Test-Path -Path $filePath) -eq $true) {
    Write-Output "File $filePath exists"
    Get-Content $filePath # gets what inside the file 
    # like with open()...
} else{
    Write-Output "File $filePath doesnt exist!" # again no f string needed
}
# so a bit complicated but 
# we capture the output of Test-Path... and then we compare it to $true 
# if it is true, then we do something in {} 
# else do something in else{}

#NOTE: you cannot do an f string like thing {$} with single quotes ''
# but if youre a weird guy you can do this (BELOW):
# Write-Host 'path `"$path"` exists
# with these weird things "``"

# you can also store the content inside a variable
if((Test-Path -Path $filePath) -eq $true) {
    Write-Output "File $filePath exists"
    $dData =Get-Content $filePath # gets what inside the file AND in var
    $dData.Count # how much lines in txt
    if($dData.Count -lt 2){
        Write-Output "this file has less than 2 lines"
    } elseif($dData.Count -le 3) {
        Write-Output "this file has 3 or less than 3 lines"
    } else {
        Write-Host "this file has $dData.Count lines"
    }
    # like with open()...
} else{
    Write-Output "File $filePath doesnt exist!" # again no f string needed
}