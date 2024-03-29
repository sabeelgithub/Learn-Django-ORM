from django.db import models


# Create your models here.

class Teacher(models.Model):  
    teacher_name = models.CharField(max_length=200)  
  
    def __str__(self):  
        return f'{self.teacher_name}' 
    

class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.IntegerField(null=True)  
    email = models.EmailField()  
    teacher_name = models.ForeignKey(Teacher, blank = True, null = True, on_delete= models.CASCADE)
    marks = models.IntegerField(default=0)
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)
    

class jobs(models.Model):
    job_name = models.CharField(max_length=100)



# abstaract-base class inheritence
class VehicleInfo(models.Model):
    name = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Vehicle(VehicleInfo):
    customer = models.ForeignKey(Student,related_name='vehicle',on_delete=models.CASCADE)


# multi-table inheritence
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Location):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# proxy model inheritence
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class MyBook(Book):

    class Meta:
        proxy = True
        ordering = ["title"]


# ordering in Meta class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)
    

class Brocamp(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)


# one to one relationship

# class Persons(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    


# class Profile(models.Model):
#     person = models.OneToOneField(Persons, on_delete=models.CASCADE)
#     bio = models.TextField()

#     def __str__(self):
#         self.person.name


# # one to many relationship
# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         self.name

# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         self.name


# # many to many 
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     courses = models.ManyToManyField('Course')
    
#     def __str__(self):
#         self.name


# class Course(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         self.name

    

    
    

