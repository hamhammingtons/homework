# this is only dedicated for strings

# strings are not just strings, they are '.NET' objects which are much more powerful than any strings 
$defaultString = "Hello there im alex"
#Case manipulation 

$defaultString.ToUpper()
$defaultString.ToLower()

#Searching and logic 

$defaultString.StartsWith("Hello") # if it starts with this
$defaultString.EndsWith("alex") # if it ends with this 
$defaultString.Contains("there") # if it has this
$defaultString.IndexOf("im") # find first index of this 
$defaultString.LastIndexOf("e") # RETURNS ONLY THE LAST FIND OF 'e' IN A STRING

$defaultString.Trim() # removes whitespaces
# # # # #
$somethingnew = $defaultString.Replace("alex", "robert") # replaces string with a new string
$somethingnew
# # # # #

$defaultString.Substring(3, 5) # gets a start index of 3 and then how much to grab (length) is 5 

$arrayOf_items = $defaultString.Split() # same as python
$arrayOf_items

$backTostring = $arrayOf_items -join " | " # basically like "|".join() but here its -join
$backTostring

$defaultString.PadRight(10, "-") # like doing str * 10 or "-" * 10 

$badString = " C:/Users/Admin/Documents/Script.PS1 "

$badString = $badString.Trim().Replace("/", "\").ToLower() # you can do this too 
$badString