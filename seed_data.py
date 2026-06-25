import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Home.settings')
django.setup()

from django.contrib.auth.models import User
from school.models import Department, Subject, Teacher, Student

def seed_data():
    print("Seeding database...")

    # Create 3 Departments
    dept1, _ = Department.objects.get_or_create(name='Science', description='Science Faculty')
    dept2, _ = Department.objects.get_or_create(name='Arts', description='Arts Faculty')
    dept3, _ = Department.objects.get_or_create(name='Commerce', description='Commerce Faculty')
    
    # Create 3 Subjects
    Subject.objects.get_or_create(name='Physics', code='PHY101', department=dept1)
    Subject.objects.get_or_create(name='History', code='HIS101', department=dept2)
    Subject.objects.get_or_create(name='Accounting', code='ACC101', department=dept3)

    # Create 3 Teachers
    user_t1, _ = User.objects.get_or_create(username='teacher1', defaults={'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'})
    if _: user_t1.set_password('teacher123'); user_t1.save()
    Teacher.objects.get_or_create(user=user_t1, department=dept1, phone='0711111111', address='123 Science Way')

    user_t2, _ = User.objects.get_or_create(username='teacher2', defaults={'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com'})
    if _: user_t2.set_password('teacher123'); user_t2.save()
    Teacher.objects.get_or_create(user=user_t2, department=dept2, phone='0722222222', address='456 Arts Blvd')

    user_t3, _ = User.objects.get_or_create(username='teacher3', defaults={'first_name': 'Robert', 'last_name': 'Brown', 'email': 'robert@example.com'})
    if _: user_t3.set_password('teacher123'); user_t3.save()
    Teacher.objects.get_or_create(user=user_t3, department=dept3, phone='0733333333', address='789 Commerce St')

    # Create 3 Students
    user_s1, _ = User.objects.get_or_create(username='student1', defaults={'first_name': 'Alice', 'last_name': 'Wonder', 'email': 'alice@example.com'})
    if _: user_s1.set_password('student123'); user_s1.save()
    Student.objects.get_or_create(user=user_s1, roll_number='S001', department=dept1, phone='0744444444', address='101 Apple St')

    user_s2, _ = User.objects.get_or_create(username='student2', defaults={'first_name': 'Bob', 'last_name': 'Builder', 'email': 'bob@example.com'})
    if _: user_s2.set_password('student123'); user_s2.save()
    Student.objects.get_or_create(user=user_s2, roll_number='S002', department=dept2, phone='0755555555', address='202 Banana Ave')

    user_s3, _ = User.objects.get_or_create(username='student3', defaults={'first_name': 'Charlie', 'last_name': 'Chaplin', 'email': 'charlie@example.com'})
    if _: user_s3.set_password('student123'); user_s3.save()
    Student.objects.get_or_create(user=user_s3, roll_number='S003', department=dept3, phone='0766666666', address='303 Cherry Ln')

    print("Database seeding complete!")

if __name__ == '__main__':
    seed_data()
