Set-StrictMode -Version latest

#arrays under a 100 elements
# use arraylist instead because arrays arent that good

$myArray = @("test1", "test2", "test3") # array

$myArray.GetType()
$myArray.IsFixedSize
# problem with arrays: whenever youre adding or removing items, ARRAYS are destroyed, and powershell creates a new one with the elements inisde
# thats why we can only use them for <100 elements. because they copy theirselves 

# $myArray # prints it out

$myArray[1] # 0 based index like in python VERY good! IF OUT OF RANGE DOESNT PRINT OUT ANYTHING, unless you do strict mode

$myArray+="elloNEW" # or $my=$my+"fewf"
$myArray=$myArray -ne "test2" # so its like- Make a list where in that list "test2" is false. which means it pops it.
# also i like how it is like dictionary method of selecting item(by mentioning them) ive never seen that before in lists
# cannot pop by index

$myArray
$myArray.Length
Write-Host "array lists start below"

# $BADLIST = [System.Collections.ArrayList]@() # this casts an array, added task in the background - bad
$myList2 = New-Object -TypeName System.Collections.ArrayList # prefer this more. it just created a new object-no tasks
# when we did GetType() it said "False" on IsFixedSize, now we can use .Add() and .D
$myList2.GetType()
$myList2.IsFixedSize

$myList2.Add("HelloWorld") # btw .add returns an index in the terminal. you will see 0.
[void]$myList2.Add("Hello New World") # when we do this we say that we want to get [void] = nothing
# so no index in the output!
Write-Host ""

$myList2.AddRange(@("test1","test3","fat")) # to add multiple items at once. 
Write-Host "Full item list before deletion:"
$myList2
Write-Host "Removing starts here"
$myList2.Remove("test3") # to delete a specific item. Only the first instance of that element will be removed!
$myList2.RemoveAt(0) # for using index to delete
$myList2.RemoveRange(0,2) # makes a slice on where to remove. ex [0-start_index, 2-items_to_cut]
# if 1 == items to cut - then we just cut the index, this is a NOTE
Write-Host ""
$myList2
$myList2.Count # we cant use length here. Only count = len(). 


$arrList = @()
$betterArray = New-Object -TypeName System.Collections.ArrayList

# Measure-Command -Expression {@(0..50000).ForEach({$arrList+=$_})} # takes like 1m:17s for an array
Measure-Command -Expression {$betterArray.AddRange(@(0..50000))} # 18 milliseconds for an array-list!

#AI COMMANDS: NEW

$myList2.Contains("fat") # like an if "item" in list: but much more simple [True/False]
$myList2.IndexOf("fat") # returns an index if found