from itertools import chain

from roster import student_roster
from classroom_organizer import ClassroomOrganizer

c = ClassroomOrganizer()

#for p in c.pairs(2):
#    print(p)

combi_4 = c.pairs(4, list=chain(c.get_students_with_subject("Math"), c.get_students_with_subject("Science")))

for c in combi_4:
    print(c)