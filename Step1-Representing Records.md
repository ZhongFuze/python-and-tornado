
### Using List

#### Start-up pointers

Lists, for example, can collect attributes about people in a positionally ordered way.


```python
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
```

We’ve just made two records, albeit simple ones, to represent two people, Bob and Sue (my apologies if you really are Bob or Sue, generically or otherwise * ). Each record is a list of four properties: name, age, pay, and job fields. To access these fields, we simply index by position; the result is in parentheses here because it is a tuple of two results:


```python
bob[0],sue[2] # fetch bob's name, sue's pay
```




    ('Bob Smith', 40000)



Processing records is easy with this representation; we just use list operations. For example, we can extract a last name by splitting the name field on blanks and grabbing the last part, and we can give someone a raise by changing their list in-place:

What's bob's last name?


```python
bob[0].split()[-1] # bob's last name
```




    'Smith'



Give sue a 25% raise!


```python
sue[2] *= 1.25 # raise 25% 
sue
```




    ['Sue Jones', 45, 50000.0, 'hardware']



#### A Database list

To collect Bob and Sue into a unit, we might simply stuff them into another list.


```python
people = [bob,sue] # reference in list of lists
for person in people: # loop
    print(person)
```

    ['Bob Smith', 42, 30000, 'software']
    ['Sue Jones', 45, 50000.0, 'hardware']
    

Now the people list represents our database. We can fetch specific records by their relative positions and process them one at a time, in loops:


```python
people[1][0]
```




    'Sue Jones'




```python
for person in people:
    print(person[0].split()[-1]) # print last name
    person[2] *= 1.20            # give each a 20% raise
```

    Smith
    Jones
    


```python
for person in people: print(person[2]) # check new pay
```

    36000.0
    60000.0
    


```python
pays = [person[2] for person in people] # collect all pay
pays
```




    [36000.0, 60000.0]




```python
pays = map((lambda x: x[2]), people)  # ditto (map is a generator in 3.X)
list(pays)
```




    [36000.0, 60000.0]




```python
sum(person[2] for person in people)   # generator expression, sum built-in
```




    96000.0



To add a record to the database, the usual list operations, such as append and extend, will suffice:


```python
people.append(['Tom', 50, 0, None])
len(people)
```




    3




```python
people[-1][0]
```




    'Tom'



Lists work for our people database, and they might be sufficient for some programs, but they suffer from a few major flaws. For one thing, Bob and Sue, at this point, are just fleeting objects in memory that will disappear once we exit Python. For another, every time we want to extract a last name or give a raise, we’ll have to repeat the kinds of code we just typed; that could become a problem if we ever change the way those operations work——we may have to update many places in our code. We’ll address these issues in a few moments.

#### Field labels

Perhaps more fundamentally, accessing fields by position in a list requires us to memorize what each position means: if you see a bit of code indexing a record on magic position 2, how can you tell it is extracting a pay? In terms of understanding the code, it might be better to associate a field name with a field value.


```python
NAME, AGE, PAY = range(3) # 0, 1 and 2
bob = ['Bob Smith', 42, 10000]
bob[NAME]
PAY,bob[PAY]
```




    (2, 10000)



This addresses readability: the three uppercase variables essentially become field names. This makes our code dependent on the field position assignments, though we have to remember to update the range assignments whenever we change record structure. Because they are not directly associated, the names and records may become out of sync over time and require a maintenance step.

We might also try this by using lists of tuples, where the tuples record both a field nameand a value; better yet, a list of lists would allow for updates (tuples are immutable).Here’s what that idea translates to, with slightly simpler records:


```python
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1]) # print name, pay
```

    Bob Smith 10000
    Sue Jones 20000
    


```python
names = [person[0][1] for person in people] # collect name
names
```




    ['Bob Smith', 'Sue Jones']




```python
for person in people:
    print(person[0][1].split()[-1]) # get last name
    person[2][1] *= 1.10            # give a 10% raise

for person in people: print(person[2])
```

    Smith
    Jones
    ['pay', 11000.0]
    ['pay', 22000.0]
    

All we’ve really done here is add an extra level of positional indexing. To do better, we might inspect field names in loops to find the one we want (the loop uses tuple assignment here to unpack the name/value pairs):


```python
for person in people:
    for (name, value) in person:
        if name == 'name':
            print(value) # find a specific field
```

    Bob Smith
    Sue Jones
    

Better yet, we can code a fetcher function to do the job for us:


```python
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label: # find a field by namme
            return fvalue
```


```python
field(bob, 'name')
```




    'Bob Smith'




```python
field(sue, 'pay')
```




    22000.0




```python
for rec in people:
    print(field(rec, 'age')) # print all ages
```

    42
    45
    

### Using Dictionaries

The list-based record representations in the prior section work, though not without some cost in terms of performance required to search for field names (assuming you need to care about milliseconds and such). But if you already know some Python, you also know that there are more efficient and convenient ways to associate property names and values. The built-in dictionary object is a natural:


```python
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
```

Now, Bob and Sue are objects that map field names to values automatically, and they make our code more understandable and meaningful. We don't have to remember what
a numeric offset means, and we let Python search for the value associated with a field' s name with its **efficient dictionary indexing**:


```python
bob['name'], sue['pay'] # not bob[0], sue[2]
```




    ('Bob Smith', 40000)




```python
bob['name'].split()[-1]
```




    'Smith'




```python
sue['pay'] *= 1.10 # raise a 10%
sue['pay']
```




    44000.0



Because fields are accessed mnemonically now, they are more meaningful to those who read your code (including you).

#### Other ways to make dictionaries

Dictionaries turn out to be so useful in Python programming that there are even more convenient ways to code them than the traditional literal syntax shown earlier—e.g.,with keyword arguments and the type constructor, as long as the keys are all strings:


```python
bob = dict(name='Bob Smith', age=42, pay=30000, jpb='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, jpb='hdw')
```


```python
bob
```




    {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'jpb': 'dev'}




```python
sue
```




    {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'jpb': 'hdw'}



by filling out a dictionary one field at a time (recall that dictionary keys are pseudo-randomly ordered):


```python
sue = {}
```


```python
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
```


```python
sue
```




    {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}



and by zipping together name/value lists:


```python
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
list(zip(names, values))
```




    [('name', 'Sue Jones'), ('age', 45), ('pay', 40000), ('job', 'hdw')]




```python
sue = dict(zip(names, values))
sue
```




    {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}



We can even make dictionaries from a sequence of key values and an optional starting value for all the keys (handy to **initialize** an empty dictionary):


```python
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')

record
```




    {'name': '?', 'age': '?', 'job': '?', 'pay': '?'}



#### Lists of dictionaries

Regardless of how we code them, we still need to collect our dictionary-based records into a database; a list does the trick again, as long as we don’t require access by key at the top level:


```python
bob
```




    {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'jpb': 'dev'}




```python
sue
```




    {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}




```python
people = [bob, sue]                                # reference in a list
for person in people:
    print(person['name'], person['pay'], sep=',')  # all name, pay
```

    Bob Smith,30000
    Sue Jones,40000
    


```python
for person in people:
    if person['name'] == 'Sue Jones':             # fetch sue's pay
        print(person['pay'])
```

    40000
    

Iteration tools work just as well here, but we use keys rather than obscure positions (in database terms, the list comprehension and map in the following code project the database on the “name” field column):


```python
names = [person['name'] for person in people]    # collect names
names
```




    ['Bob Smith', 'Sue Jones']




```python
list(map((lambda x: x['name']), people))         # ditto, generate
```




    ['Bob Smith', 'Sue Jones']




```python
sum(person['pay'] for person in people)          # sum all pay
```




    70000



Interestingly, tools such as list comprehensions and on-demand generator expressions can even approach the utility of SQL queries here, albeit operating on in-memory objects:


```python
[rec['name'] for rec in people if rec['age'] >= 45] # SQL-ish query
```




    ['Sue Jones']




```python
[(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
```




    [42, 2025]




```python
G = (rec['name'] for rec in people if rec['age'] >= 45)
G
```




    <generator object <genexpr> at 0x0000021461B369E8>




```python
next(G)
```




    'Sue Jones'




```python
G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
G
```




    <generator object <genexpr> at 0x0000021461B36FC0>




```python
G.__next__()
```




    42



And because dictionaries are normal Python objects, these records can also be accessed and updated with normal Python syntax:


```python
for person in people:
    print(person['name'].split()[-1]) # last name
    person['pay'] *= 1.10
```

    Smith
    Jones
    


```python
for person in people: print(person['pay'])
```

    33000.0
    44000.0
    

#### Nested structures

we could avoid the last-name extraction code in the prior examples by further structuring our records. Because all of Python’s compound datatypes can be nested inside each other and as deeply as we like, we can build up fairly complex information structures easily—simply type the object’s syntax, and Python does all the work of building the components, linking memory structures, and later reclaiming their space. 

The following, for instance, represents a more structured record by nesting a **dictionary**, **list**, and **tuple** inside another dictionary:


```python
bob2 = {'name':{'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}
```


```python
bob2['name']                            # bob's full name
```




    {'first': 'Bob', 'last': 'Smith'}




```python
bob2['name']['last']                    # bob's last name
```




    'Smith'




```python
bob2['pay'][1]                          # bob's upper pay
```




    50000



The name field is another dictionary here, so instead of splitting up a string, we simply index to fetch the last name. Moreover, people can have many jobs, as well as minimum and maximum pay  limits. In fact, Python becomes a sort of query language in such cases—we can fetch or change nested data with the usual object operations:


```python
for job in bob2['job']: print(job)     # all of bob's jobs
```

    software
    writing
    


```python
bob2['job'][-1]                       # bob's last job
```




    'writing'




```python
bob2['job'].append('janitor')         # bob's gets a new job
bob2
```




    {'name': {'first': 'Bob', 'last': 'Smith'},
     'age': 42,
     'job': ['software', 'writing', 'janitor'],
     'pay': (40000, 50000)}



It’s OK to grow the nested list with append , because it is really an independent object. Such nesting can come in handy for more sophisticated applications; to keep ours simple, we’ll stick to the original flat record structure.

#### Dictionaries of dictionaries

One last twist on our people database: we can get a little more mileage out of dictionaries here by using one to represent the database itself. That is, we can use a **dictionary of dictionaries**—the outer dictionary is the database, and the nested dictionaries are the records within it. Rather than a simple list of records, a dictionary-based database allows us to store and retrieve records by symbolic key:


```python
bob = dict(name='Bob Smith', age=42, pay=30000, jpb='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, jpb='hdw')
bob
```




    {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'jpb': 'dev'}




```python
db={}
db['bob'] = bob               # reference in a dict of dicts
db['sue'] = sue
```


```python
db['bob']['name']             # fetch bob's name
```




    'Bob Smith'




```python
db['sue']['pay'] = 50000      # change sue's pay
```


```python
db['sue']['pay']              # fetch sue's pay
```




    50000




```python
import pprint
pprint.pprint(db)
```

    {'bob': {'age': 42, 'jpb': 'dev', 'name': 'Bob Smith', 'pay': 30000},
     'sue': {'age': 45, 'jpb': 'hdw', 'name': 'Sue Jones', 'pay': 50000}}
    

If we still need to step through the database one record at a time, we can now rely on  dictionary iterators. In recent Python releases, a dictionary iterator produces one key in a for loop each time through (for compatibility with earlier releases, we can also call the db.keys method explicitly in the for loop rather than saying just db , but since Python 3’s keys result is a generator, the effect is roughly the same):


```python
for key in db:
    print(key,'=>', db[key]['name'])
```

    bob => Bob Smith
    sue => Sue Jones
    


```python
for key in db:
    print(key,'=>', db[key]['pay'])
```

    bob => 30000
    sue => 50000
    


```python
for key in db:
    print(key,'=>', db[key]['name']) 
```

    bob => Bob Smith
    sue => Sue Jones
    

To visit all records, either index by key as you go:


```python
for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10
```

    Smith
    Jones
    

or step through the dictionary’s values to access records directly:


```python
for record in db.values(): print(record['pay'])
```

    33000.0
    55000.00000000001
    


```python
x = [db[key]['name'] for key in db]
x
```




    ['Bob Smith', 'Sue Jones']




```python
x = [rec['name'] for rec in db.values()]
x
```




    ['Bob Smith', 'Sue Jones']



And to add a new record, simply assign it to a new key; this is just a dictionary, after all:


```python
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
```


```python
db['tom']
```




    {'name': 'Tom', 'age': 50, 'job': None, 'pay': 0}




```python
db['tom']['name']
```




    'Tom'




```python
list(db.keys())
```




    ['bob', 'sue', 'tom']




```python
len(db)
```




    3




```python
[rec['age'] for rec in db.values()]
```




    [42, 45, 50]




```python
[rec['name'] for rec in db.values() if rec['age'] >= 45]  # SQL-ish query
```




    ['Sue Jones', 'Tom']


