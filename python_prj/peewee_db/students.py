from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    # tell model what db it belongs to
    class Meta:
        database = db


students = [
    {'username': 'kennethlove',
     'points': '14888'},
    {'username': 'chalkers',
     'points': '11915'},
    {'username': 'joykesten2',
     'points': '7363'},
    {'username': 'craigdennis',
     'points': '4079'},
    {'username': 'davemcfarland',
     'points': '14717'},
]


def add_students():
    for student in students:
        try:
            # create a record
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            # get a single record
            student_record = Student.get(username=student['username'])  # get() ONE record / the first record
            if student['points'] > student_record.points:
                # update record
                student_record.points = student['points']
                student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)  # safe - stops error if code is run and table already created
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))
