# hash tables are k:v pairs 

$myHashTable = @{
    key1 = 100
    key2 = 2.34
    name = 'Jone joe'
    key3 = $true
}

$myHashTable.GetType()
# now to get only keys and only values- its the same as python
# python: table.keys or table.values
# but in poweshell its just uppercase: table.Keys, table.Values

$myHashTable.Keys # for some reason they arent ordered, like a set. we just check if the key exists
$myHashTable.Values
# $myHashTable.GetEnumerator() # now this is like table.items() in python. I like this! or just call it 

# how to get value of a key 

Write-Host ""
$myHashTable.key3 # just by mentioning it 
$myHashTable['key3'] # and you can do this too

#Problem with finding if a key exists 
# now powershell is very lazy again and it cant help you check if a key exists by throwing an error via strict mode
# so we cant really do that, however we can do a thing called table.Contains... we can check a key and a value or items
# via that 

$myHashTable.ContainsKey("key4") # returns false because doesnt exist 
# $myHashTable.ContainsValue # i dont think i need it 

# similarity: dictionaries cannot have dupes 


# how to add items 

$myHashTable.Add('key19','testing add')
$myHashTable["key20"] = "testing python add" # now this is much more similar to python 
$myHashTable.key21 = "testing dot function add" # easier than .add but uhh idk about the compatability
# warning: again they arent ordered.

#change values 

$myHashTable.key2 = 8134 # change value 

$myHashTable.Remove("key3")
# interesting can we do like $myHashTable["key3"]= $null and it will delete it like that? 
# answer: NO.

$myHashTable


############# CUSTOM OBJ ###############

# my hypothosis: its like creating a class and you have __init__() as this add-member thing 
$employee1 = New-Object -TypeName PSCustomObject
$employee1.GetType()

Add-Member -InputObject $employee1 -MemberType NoteProperty -Name "EmployeeID" -Value "1001"
Add-Member -InputObject $employee1 -MemberType NoteProperty -Name "FirstName" -Value "Penny"
Add-Member -InputObject $employee1 -MemberType NoteProperty -Name "Title" -Value "CEO"

$employee1 
# uses same notation as hash tables 

$employee1.FirstName
# more useful Get-Member 
Get-Member -InputObject $employee1 # its like dir() mixed with data types 
$employee2 = [PSCustomObject]@{ # were creating a hash table and then casting it to a pscustomobject - which is very good
    EmployeeId='101'
    FirstName = 'Jeremy'
    Title = "ceo2"
}
$employee2.FirstName # doesnt suggest that FirstName is a thing  but works
# WHY ^^^ because ps is dynamic, meaning that if you run it once it will rememeber the object and you can use 
# .FirstName or other properties. WORKED: 

#IF YOU want a single line hashtable casting thing, youll have to do a semicolon after youve made a new property\
# hello = ""; jeremy = '' thats it