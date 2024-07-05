from app1.models import Employee


# exec(open(r'F:\django_framework1\first_project\app1\db_shell.py').read())

# for read all
# all_emps = Employee.objects.all()
# print(all_emps)

# for emp in all_emps:
#     print(emp.name)

# # single read
# try:
#     emp = Employee.objects.get(id=4)
#     print(emp)
# except Employee.DoesNotExist:
#     print("employee with given id is doesnot exist ingiven database")

# create
# 1st way
# emp = Employee(
#     name="c", email="c@gmail.com", mobile_num=12345, designation="tester", salary=1200
# )
# emp.save()

# 2nd way
# Employee.objects.create(name="D", email="d@gmail.com", mobile_num=1245645, designation="manager", salary=1280
# )


# update
# try:
#     emp = Employee.objects.get(id=1)
#     emp.salary=3425
#     emp.save()
# except Employee.DoesNotExist:
#     print("employee with given id is doesnot exist ingiven database")


# delete
# try:
#     emp = Employee.objects.get(id=4)
#     emp.delete()
# except Employee.DoesNotExist:
#     print("employee with given id is doesnot exist ingiven database")

# read
# emp = Employee.objects.filter(email="aaa@gmail.com")
# print(emp)  #search by filter   #we got empty set becoz we don't have this gmmail

emp = Employee.objects.get(email="aaa@gmail.com")
print(emp)  #this gives error becoz we don't have this email
