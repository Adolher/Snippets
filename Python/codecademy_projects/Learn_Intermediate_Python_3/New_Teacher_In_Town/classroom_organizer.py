import itertools
from tkinter import N
from roster import student_roster

class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.sorted_names):
            raise StopIteration
        else:
            return self.sorted_names[self.index]

    def _sort_alphabetically(self,students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students

    def pairs(self, x, list=None):
        if list is not None:
            return itertools.combinations(list, x)
        else:
            return itertools.combinations(self.sorted_names, x)