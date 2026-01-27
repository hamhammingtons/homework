$filePath = "C:\Users\Admin\OneDrive\Рабочий стол\Python, tasks done by me\howework_for_itstep\libraries\powershel_lol\data.txt"

$dataContent = Get-Content -Path $filePath # with open() thing 

$dataContent.Count
$firstName = $dataContent[1] # data = array (automatically .split i guess)

if($firstName -eq "hello"){
    Write-Output "My name is $($firstName)"
} elseif ($firstName -eq "world") {
    Write-Output "I am world"
}else {
    Write-Output "idk"
}

$firstName = "world"
switch($firstName){ # so i guess its like match-case...
    "world"{
        Write-Output "I am world"
        break
    }
    "how are you"{
        Write-Output "my name is how are you"
        break
    }
    default{
        Write-Output "idk"
        break
    }
}
# if you want only 1 value being checked and thats it, do a break.

#swtich($dataContent.Count){
    #(-lt 2){
       # Write-Output "bad"
    #}
#}
# ^^ WRONG
# we must do a curly bracket if were doing an evaluation! 

switch($dataContent.Count){
    {$_ -lt 2}{
        Write-Output "This works and it is good!"
        break
    }

    default{
        Write-Output "thing is $($_) lines"
        break
    }
}


################ NEW INSTEAD OF FOR... RANGE THING ##################

Write-Host (8..10) 
# will do [i for i in range(8+1, 10)]
# this double dot is so much more compact AND it creates an array.

$myArrsimplified = (1..10) # @(1,2,3,4...)

# to count backwards
$myReversed_arr = (10..1)


### NEW STUFF ###

# how switch statement differs from python is 
# in python, match can only take 1 value 
# a swtich statement however, can take arrays, as an example.

$myNumbers = 1..5
switch ($myNumbers) {

    3 { "Found the number 3!" }
    { $_ % 2 -eq 0 } { "$_ is Even" } # works as a pipeline!
    # i mean the $_ part. 
}

# FUN YUM

$string = "fun yum"

switch -Wildcard ($string){
    "f*"{Write-Output "starts with f"}
    "*yum" {Write-Output "ends with yum"}
}

# wildcard is used when you need to check if starts with, ends with