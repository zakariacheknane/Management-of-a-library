from django.db import models

class Student(models.Model):
    id_student= models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    Registration_date = models.DateField()

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    gender= models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Loan(models.Model):
    id_loan = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"Loan of {self.book_id} by {self.student_id}"
