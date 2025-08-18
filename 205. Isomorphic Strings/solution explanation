class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize two hashmaps for s -> t and t -> s mappings
        mapST, mapTS = {}, {}

        # Loop through both strings simultaneously
        for s1, t1 in zip(s, t):
            # when we zip its like egg and add where it will be {"e" , "a"} {"g" , "d"} {"g" , "d"}
            # Check for conflicts in both mappings
            # Conflict occurs if:
            # 1. s1 was previously mapped to a different t1. e.g. like e with g and then e with d 
            # 2. t1 was previously mapped from a different s1. like d with g and d with e 
            # characther must be mapped once to a charachter no charachter is allowed to be mapped with different charachters
            if (s1 in mapST and mapST[s1] != t1) or (t1 in mapTS and mapTS[t1] != s1):
                return False  # Conflict found, strings are not isomorphic

            # If no conflict, create/update the mappings
            mapST[s1] = t1  # map character from s to t
            mapTS[t1] = s1  # map character from t to s
        
        # If loop completes without conflicts, strings are isomorphic
        return True


 # The loop starts with empty hashmaps and keeps filling them as we go
 # We don't map before checking to avoid overwriting mappings incorrectly

How it works step by step:
Start with empty hashmaps:

mapST = {}  # s → t
mapTS = {}  # t → s


Initially, nothing is mapped.

# First iteration:

s1, t1 = 'e', 'a'  # from s = "egg", t = "add"
Check for conflict:
s1 in mapST  # False, because mapST is empty
t1 in mapTS  # False, because mapTS is empty
No conflict found → we add the mapping:

mapST['e'] = 'a'
mapTS['a'] = 'e'

# Second iteration:

s1, t1 = 'g', 'd'
Check for conflict:

'g' in mapST  # False
'd' in mapTS  # False
No conflict → add mapping:
mapST['g'] = 'd'
mapTS['d'] = 'g'

# Third iteration:
s1, t1 = 'g', 'd'
Check for conflict:

'g' in mapST → True, mapST['g'] == 'd' ✅ matches  
'd' in mapTS → True, mapTS['d'] == 'g' ✅ matches
No conflict → mappings stay the same.