#
from collections import OrderedDict
roll_no=OrderedDict([
	(11,'Shubham'),
	(9,'Pankaj'),
	(17,'JournalDev')])
for key,value in roll_no.items():
	print(key,value)

from collections import defaultdict
marks = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]
 dict_marks=defaultdict(list)
for key ,value in marks:
	dict_marks[key].append(value)
print(list(dict_marks.items()))
#Collection counter allows yous to easliy count objects.
from collections import Counter
count =Counter(name for name,marks in marks)
print(count)

from collections import namedtuple
User=namedtuple('User','name age gender')
shubham=User(name='Shubham',age=23,gender='M')
print(shubham)
print('Name of User:{0}'.format(shubham.name))
#################Deque
from collections import deque
name=deque('Shubham')
print('Deque  :',name)
print('Queue length:',len(name))
print('left part :',name[0])
print('Right part :',name[-1])
name.remove('b')
print('remove(b):',name)