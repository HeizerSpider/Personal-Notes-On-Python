Compilation of Python Notes  

Topics covered:  
- Tuples  
- Dictionary  
- Arrays  
- List Comprehension  

### Tuples
Somewhat like a list, with values separated by commas and accessed by integers  
```
Tuple = ('hi' , 'world')  

### Dictionary

- Unordered collection of data values (key:value pair)  
```
Dict = {1: 'Hello', 2: 'World', 3: [1,2,3,4], 'Hello': 'World'}
```

- Dictionary is created by placing key:value pairs within curly braces {}  
- The key and value can be a string, integer, array and even have another dictionary nested within in  
- Adding to a dictionary:  
```
Dict[Key]= Value  
```

- Deleting from dictionary (pop-ed element can be assigned to a variable and be used as well):  
```
element = Dict.pop(1)  
print(element) #will return 'Hello' based on Dict above  
```

Other useful Dictionary methods:
|Methods|Descriptions|
|-------|------------|
|copy()|Shallow copy of dictionary (shallow means that the copied item is of the same area of memory)|
|clear()|Deletes all items at once|
|popitem()|Removes key value pair and returns it as a tuple|
|get()|Accessing a value for a key|
|dictionary_name.values()|returns a list of all values in a dictionary|
|str()|produces a string representation of a dictionary|
|update()|Adds another dictionary to the main one|


### Array
- All elements of an array must be of the same type  
- Array module must be imported  
- 
```
import array as arr

#array with int type
a = arr.array('i', [1,2,3])
#f for float, many others included

print(a[0]) #1 will be printed
```




