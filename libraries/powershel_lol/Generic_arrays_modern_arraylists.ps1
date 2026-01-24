# Generic lists are like arraylists, but they are for specific data types.
# it is a rule which means: [there will be only 1 data type and thats it]

$stringList = New-Object System.Collections.Generic.List[string]
$intList = New-Object System.Collections.Generic.List[int]

$stringList.GetType() # list'1 for some reason idk why 

# cool features of generic lists
# 1. Generic Lists are quiet. meaning that they dont need [void]
# 2. prevents type checking bugs, rejects eveyrthing besides what is stated in list[DATA_TYPE]
# 3. much more faster than everything else because we stated that it will only have strings. mr pc will like that and exe-
# cute faster

$intList.AddRange([int[]]@(10, 5, 100, 2)) # whilst doing this specify that its an int array. powershell is very lazy.
$intList.Sort()
$intList

Measure-Command -Expression {$intList.AddRange([int[]]@(0.50000))}