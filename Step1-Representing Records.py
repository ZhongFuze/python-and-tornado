#!/usr/bin/env python
# coding: utf-8

# ### Using List

# #### Start-up pointers

# Lists, for example, can collect attributes about people
# in a positionally ordered way.

# In[1]:
import pprint

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']


# # We’ve just made two records, albeit simple ones, to represent two people,
# Bob and Sue (my apologies if you really are Bob or Sue, generically
# or otherwise * ).Each record is a list of four properties: name, age,
# pay, and job fields. To access these fields, we simply index by position;
# the result is in parentheses here because it is a tuple of two results:

# In[2]:

# fetch bob's name, sue's pay
bob[0], sue[2]


# Processing records is easy with this representation; we just use
# list operations. For example, we can extract a last name by splitting
# the name field on blanks and grabbing the last part, and we can give
# someone a raise by changing their list in-place:

# What's bob's last name?

# In[3]:

# bob's last name
bob[0].split()[-1]


# Give sue a 25% raise!

# In[4]:

# raise 25%
sue[2] *= 1.25
sue


# #### A Database list

# To collect Bob and Sue into a unit, we might simply
# stuff them into another list.

# In[5]:

# reference in list of lists
# loop
people = [bob, sue]
for person in people:
    print(person)


# Now the people list represents our database. We can fetch specific records by
# their relative positions and process them one at a time, in loops:

# In[6]:


people[1][0]


# In[7]:


for person in people:
    print(person[0].split()[-1])      # print last name
    person[2] *= 1.20                 # give each a 20% raise


# In[8]:


for person in people:
    print(person[2])     # check new pay


# In[9]:


pays = [person[2] for person in people]      # collect all pay
pays


# In[10]:


pays = map((lambda x: x[2]), people)  # ditto (map is a generator in 3.X)
list(pays)


# In[11]:


sum(person[2] for person in people)   # generator expression, sum built-in


# To add a record to the database, the usual list operations,
# such as append and extend, will suffice:

# In[12]:


people.append(['Tom', 50, 0, None])
len(people)


# In[13]:


people[-1][0]


# Lists work for our people database, and they might be sufficient for some
# programs, but they suffer from a few major flaws. For one thing, Bob and Sue,
#  at this point, are just fleeting objects in memory that will disappear once
#  we exit Python. For another, every time we want to extract a last name
#  or give a raise, we’ll have to repeat the kinds of code we just typed;
#  that could become a problem if we ever change the way those operations
#  work——we may have to update many places in our code. We’ll address
#  these issues in a few moments.

# #### Field labels

# Perhaps more fundamentally, accessing fields by position in a list requires
# us to memorize what each position means: if you see a bit of code indexing
# a record on magic position 2, how can you tell it is extracting a pay?
# In terms of understanding the code, it might be better to associate a
# field name with a field value.

# In[14]:


NAME, AGE, PAY = range(3)         # 0, 1 and 2
bob = ['Bob Smith', 42, 10000]
bob[NAME]
PAY, bob[PAY]


# This addresses readability: the three uppercase variables essentially
# become field names. This makes our code dependent on the field position
# assignments, though we have to remember to update the range assignments
# whenever we change record structure. Because they are not directly associated
# the names and records may become out of sync over time and require a
# maintenance step.

# We might also try this by using lists of tuples, where the tuples record
# both a field nameand a value; better yet, a list of lists would allow
# for updates (tuples are immutable).Here’s what that idea translates to
# , with slightly simpler records:

# In[15]:


bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1])            # print name, pay


# In[16]:


names = [person[0][1] for person in people]      # collect name
names


# In[17]:


for person in people:
    print(person[0][1].split()[-1])              # get last name
    person[2][1] *= 1.10                         # give a 10% raise

for person in people:
    print(person[2])


# All we’ve really done here is add an extra level of positional indexing.
# To do better, we might inspect field names in loops to find the one we
# want (the loop uses tuple assignment here to unpack the name/value pairs):

# In[18]:


for person in people:
    for (name, value) in person:
        if name == 'name':
            print(value)                        # find a specific field


# Better yet, we can code a fetcher function to do the job for us:

# In[19]:


def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:                     # find a field by namme
            return fvalue


# In[20]:


field(bob, 'name')


# In[21]:


field(sue, 'pay')


# In[22]:


for rec in people:
    print(field(rec, 'age'))                  # print all ages


# ### Using Dictionaries

# The list-based record representations in the prior section work, though not
# without some cost in terms of performance required to search for field names
# (assuming you need to care about milliseconds and such). But if you already
# know some Python, you also know that there are more efficient and convenient
# ways to associate property names and values. The built-in dictionary object
# is a natural:

# In[23]:


bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}


# Now, Bob and Sue are objects that map field names to values automatically,
# and they make our code more understandable and meaningful.
# We don't have to remember what
# a numeric offset means, and we let Python search for the value associated
# with a field' s name with its **efficient dictionary indexing**:

# In[24]:


bob['name'], sue['pay']                   # not bob[0], sue[2]


# In[25]:


bob['name'].split()[-1]


# In[26]:


sue['pay'] *= 1.10                        # raise a 10%
sue['pay']


# Because fields are accessed mnemonically now, they are more meaningful
# to those who read your code (including you).

# #### Other ways to make dictionaries

# Dictionaries turn out to be so useful in Python programming that there are
# even more convenient ways to code them than the traditional literal syntax
# shown earlier—e.g.,with keyword arguments and the type constructor, as long
# as the keys are all strings:

# In[27]:


bob = dict(name='Bob Smith', age=42, pay=30000, jpb='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, jpb='hdw')


# In[28]:


bob


# In[29]:


sue


# by filling out a dictionary one field at a time (recall that
# dictionary keys are pseudo-randomly ordered):

# In[30]:


sue = {}


# In[31]:


sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'


# In[32]:


sue


# and by zipping together name/value lists:

# In[33]:


names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
list(zip(names, values))


# In[34]:


sue = dict(zip(names, values))
sue


# We can even make dictionaries from a sequence of key values and an
# optional starting value for all the keys (handy to **initialize**
# an empty dictionary):

# In[35]:


fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')

record


# #### Lists of dictionaries

# Regardless of how we code them, we still need to collect our dictionary-based
# records into a database; a list does the trick again, as long as we don’t
# require access by key at the top level:

# In[36]:


bob


# In[37]:


sue


# In[38]:


people = [bob, sue]                                # reference in a list
for person in people:
    print(person['name'], person['pay'], sep=',')  # all name, pay


# In[39]:


for person in people:
    if person['name'] == 'Sue Jones':             # fetch sue's pay
        print(person['pay'])


# Iteration tools work just as well here, but we use keys rather
# than obscure positions (in database terms, the list comprehension
# and map in the following code project the database on the
# “name” field column):

# In[40]:


names = [person['name'] for person in people]    # collect names
names


# In[41]:


list(map((lambda x: x['name']), people))         # ditto, generate


# In[42]:


sum(person['pay'] for person in people)          # sum all pay


# Interestingly, tools such as list comprehensions and on-demand
# generator expressions can even approach the utility of SQL
# queries here, albeit operating on in-memory objects:

# In[43]:


[rec['name'] for rec in people if rec['age'] >= 45]         # SQL-ish query


# In[44]:


[(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]


# In[45]:


G = (rec['name'] for rec in people if rec['age'] >= 45)
G


# In[46]:


next(G)


# In[47]:


G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
G


# In[48]:


G.__next__()


# And because dictionaries are normal Python objects, these records 
# can also be accessed and updated with normal Python syntax:

# In[49]:


for person in people:
    print(person['name'].split()[-1])                        # last name
    person['pay'] *= 1.10


# In[50]:


for person in people: print(person['pay'])


# #### Nested structures

# we could avoid the last-name extraction code in the prior examples by further
# structuring our records. Because all of Python’s compound datatypes can be
# nested inside each other and as deeply as we like, we can build up fairly
# complex information structures easily—simply type the object’s syntax, and
# Python does all the work of building the components, linking memory
# structures, and later reclaiming their space.
# The following, for instance, represents a more structured record by
# nesting a **dictionary**, **list**, and **tuple** inside another dictionary:

# In[51]:


bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}


# In[52]:


bob2['name']                            # bob's full name


# In[53]:


bob2['name']['last']                    # bob's last name


# In[54]:


bob2['pay'][1]                          # bob's upper pay


# The name field is another dictionary here, so instead of splitting up a
# string, we simply index to fetch the last name. Moreover, people can have
# many jobs, as well as minimum and maximum pay  limits. In fact, py becomes
# a sort of query language in such cases—we can fetch or change nested data
# with the usual object operations

# In[55]:


for job in bob2['job']:
    print(job)     # all of bob's jobs


# In[56]:


bob2['job'][-1]                       # bob's last job


# In[57]:


bob2['job'].append('janitor')         # bob's gets a new job
bob2


# It’s OK to grow the nested list with append , because it is really
# an independent object. Such nesting can come in handy for more
# sophisticated applications; to keep ours simple, we’ll stick to
# the original flat record structure.

# #### Dictionaries of dictionaries

# One last twist on our people database: we can get a little more mileage
# out of dictionaries here by using one to represent the database itself.
# That is, we can use a **dictionary of dictionaries**—the outer dictionary
# is the database, and the nested dictionaries are the records within it.
# Rather than a simple list of records, a dictionary-based database allows
# us to store and retrieve records by symbolic key:

# In[58]:


bob = dict(name='Bob Smith', age=42, pay=30000, jpb='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, jpb='hdw')
bob


# In[59]:


db = {}
db['bob'] = bob               # reference in a dict of dicts
db['sue'] = sue


# In[60]:


db['bob']['name']             # fetch bob's name


# In[61]:


db['sue']['pay'] = 50000      # change sue's pay


# In[62]:


db['sue']['pay']              # fetch sue's pay


# In[63]:

pprint.pprint(db)


# If we still need to step through the database one record at a time,
# we can now rely on  dictionary iterators. In recent Python releases,
# a dictionary iterator produces one key in a for loop each time through
# (for compatibility with earlier releases, we can also call the db.keys
# method explicitly in the for loop rather than saying just db ,
# but since Python 3’s keys result is a generator,
# the effect is roughly the same):

# In[64]:


for key in db:
    print(key, '=>', db[key]['name'])


# In[65]:


for key in db:
    print(key, '=>', db[key]['pay'])


# In[66]:


for key in db:
    print(key, '=>', db[key]['name'])


# To visit all records, either index by key as you go:

# In[67]:


for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10


# or step through the dictionary’s values to access records directly:

# In[68]:


for record in db.values():
    print(record['pay'])


# In[69]:


x = [db[key]['name'] for key in db]
x


# In[71]:


x = [rec['name'] for rec in db.values()]
x


# And to add a new record, simply assign it to a new key;
# this is just a dictionary, after all:

# In[72]:


db['tom'] = dict(name='Tom', age=50, job=None, pay=0)


# In[73]:


db['tom']


# In[74]:


db['tom']['name']


# In[75]:


list(db.keys())


# In[76]:


len(db)


# In[77]:


[rec['age'] for rec in db.values()]


# In[78]:


[rec['name'] for rec in db.values() if rec['age'] >= 45]  # SQL-ish query


# In[ ]:
