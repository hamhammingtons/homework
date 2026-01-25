$myVariable = "Jocker MR man" # variables start with $
# variables are automatcially printed out without Write-Host, you just have to call them 
# like $myVal = prints out the value 
# Note from ai: in powershell almost eveyrthing is an object
# ^ the object has its own: 1. methods (.toLower()) 2. properties (length)
$intVariable = 1 # int is a 32 bit integer
$doubleVariable = 1.14 # double is a float 

$newVar=$myVariable.ToLower() # when you do just $myvariable.lower() it doesnt change myvariable, it just prints out it lowered
# so here i assign it instead ^^^ 
$newVar.GetType()
$intVariable.GetType()
$doubleVariable.GetType()

$tV = 10 # ten value
$fV = 5 # five value

$res = $tV + $fV # However, it doesnt output anything here, because we are storing the values. ^^^^^^
$res # now we call it and it prints out the value

# bools
# bools are defined via $thing = $true, not just 'true'. also note: you cant assign values as pre-built in things 
# $true = 1 : ERROR!!!!!

$hello = $true # ^^^

# ok so there is no == in powershell, but you can do this however (look below)

($tV -eq $fV) # -eq = equals to, basically ==
# you can also mass attach to check types for example
# ($tV -eq $fV).GetType() -- type bool [true or false]

($nothingNull -eq $null) # you can also do type checking with just this!

#modes:
# there are also modes for type checking, for example lua has this too
# --strict -> checks for everything.
# in the case that a variable doesnt exists, it will return null, if we do Set-StrictMode -Version latest (BELOW)
# it will make so if a variable hasnt been assigned it returns an error.

Write-Host "fatval, evenfatter below"
[int]$fatVal = 1.2 # just like int(val) but here we do [] so we: "declare: we only want these values"
# wait no, even easier: we can explain it by like val: int = 1.2 but it actually int()'s it 
$fatVal.GetType()

[double]$evenFatter = 1 

$evenFatter.GetType()

# we can also assign vars to commandlets 

$commDate = Get-Date
$commDate