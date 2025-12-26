security_log: list[tuple] = [("Alice", "Lab", "00:90"), ("badguy", "lab", "125421")]

for i, (name, place, time) in enumerate(security_log):
    print(f"Log #{i}: {name} entered the {place}")

# or list comprehension

print({name for name, place, time in security_log})  # only names SHOULD BE UNIQUE
# REAZLIED:
"""for loops jsut get the first variable without a doubt, meanin they fetch the first thing. so for example if our list (or anything esle)
   has list = [(jfqeuj), (uqefuoq)], in a for loop like 
   for qdw,dqw,dqw in list
   it automatically gets the first thing and doesnt really need an iterator like x to get the whole tuple, if you need to get one
   
   what i mean is that python uses 2 things 
   for x in list:    -- this is getting the 1 thing where the variable x will catch the tuple. for example ("hello", "there"); without unpacking
                                        meaning that you will need to do it manually
   
   for x,y in list:  -- this is getting the whole thing AND its items. for example:
                        ("hello", "there", and python will get x="hello", y="there") whsile in a single thing(tuple) of the for loop)
                        without needing to manualyl set up a thing like name = x[0]..."""
