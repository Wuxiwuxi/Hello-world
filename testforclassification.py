class Person(object):
    def __init__(self,name,studentid,date,gender):
        self.name = name
        self.studentid = studentid
        self.date = date
        self.gender = gender

# check if student's id is valid
# in this case if it is too old, it is not valid
# take 0 as an example
def check(id):
    if id[1]==  "0":
        return "not valid\n"
    else :
        return "valid"



f = open(r"/home/taoyongxue/Downloads/test.txt")
lines = f.readlines()

'''
#ugly code at first attempt
#block 1
words = lines[0].split()
name = words[1]
studentid = words[3]
date = words[2]
print name,studentid,date

# block 2
words = lines[1].split()
name = words[1]
studentid = words[3]
date = words[2]
print name,studentid,date
'''

people = []
for line in lines:
    words = line.split()
    people.append(Person(words[1],words[4],words[3],words[2]))
#people = [p1,p2,p3,p4.......]


for person in people:
    print "Name: {} Id: {} gender: {} date: {} verification: {}".format(person.name, person.studentid, person.gender,person.date,check(person.studentid))

