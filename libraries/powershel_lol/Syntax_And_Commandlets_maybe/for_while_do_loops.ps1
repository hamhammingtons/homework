
for($counter=0; $counter -lt 10; $counter=$counter+=2 ){
    Write-Output $counter
}
# so counter var gets assigned first, second is the condition 
# and then we do $counter++ so it adds +1 to counter 
# 10 is inclusive

$arr = @("steve","john","tim")

for($i=0; $i -lt $arr.Length; $i++){
    Write-Output $arr[$i] += "Doe" # linear search thing
    # so what it does it gets the string and then adds Doe to it
    # like " Doe".join(str)
    # or str + str 
}
$arr

###### PROBLEM WITH FOREACH
# In the code below, we can say that 
# foreach doesnt actually apply changes to the item, only to the 
# iterable value. 

foreach($item in $arr){
    $item += "test"
}

$arr

Get-Date
while((Get-Date).Minute -eq 31){ # inside the while () the condition needs to be stated
    Get-Date
} # as long as the minute is 31, it will do this. then if its 32 it will break

while($true){
    Write-Output "welcome to the parraot application"
    Write-Output "enter 'q' to quit"

    $input = Read-Host -Prompt "Enter here: "
    if($input -eq "q"){
        break
    }
    Write-Output "entered $input"
}


#WHILE DO

# cool thing with these they will be at least exectued once 
# even if the cond is false 
do{
    $input = Read-Host -Prompt "plz enter a thing" 
    Write-Output "youve enterred $input"
} while($input -ne "q")


# DO UNTIL - like lua
# only while loops whenever a condition is false 
do {
    
} until($true) # cond inside until - only executes once because of true  