from django.http import HttpResponse
from django.shortcuts import render,redirect
from listings.models import Student,Book,Loan

# Create your views here.
def student(request):
     students=Student.objects.all()
     return render(request, 'student.html',{'students':students})

def addStudent(request):
   if(request.method=='POST'):
          lastname=request.POST.get('lastname')
          firstname=request.POST.get('firstname')
          Registration_date=request.POST.get('Registration_date')
          new_student=Student(lastname=lastname,firstname=firstname,Registration_date=Registration_date)
          new_student.save()
          return redirect("Student")
   return render(request, 'student.html')

def updateStudent(request,id):
     if(request.method=='POST'):
          lastname=request.POST.get('lastname')
          firstname=request.POST.get('firstname')
          Registration_date=request.POST.get('Registration_date')
          new_student=Student(id_student=id,lastname=lastname,firstname=firstname,Registration_date=Registration_date)
          new_student.save()
          return redirect("Student")
     return render(request, 'student.html')

def deleteStudent(request,id):
     student=Student.objects.get(id_student=id)
     student.delete()
     return redirect("Student")
     
def book(request):
     books=Book.objects.all()
     return render(request, 'book.html',{'books':books})

def addBook(request):
   if(request.method=='POST'):
          title=request.POST.get('title')
          author=request.POST.get('author')
          section=request.POST.get('section')
          gender=request.POST.get('gender')
          available=request.POST.get('available')
          new_book=Book(title=title,author=author,section=section,gender=gender,available=available)
          new_book.save()
          return redirect("Book")
   return render(request, 'book.html')

def updateBook(request,id):
      if(request.method=='POST'):
          title=request.POST.get('title')
          author=request.POST.get('author')
          section=request.POST.get('section')
          gender=request.POST.get('gender')
          available=request.POST.get('available')
          new_book=Book(id_book=id,title=title,author=author,section=section,gender=gender,available=available)
          new_book.save()
          return redirect("Book")
      return render(request, 'book.html')
 
def deleteBook(request,id):
     book=Book.objects.get(id_book=id)
     book.delete()
     return redirect("Book")

def loan(request):
     loans=Loan.objects.all()
     students=Student.objects.all()
     books=Book.objects.all()
     return render(request, 'loan.html',{'loans':loans,'students':students,'books':books})

def addLoan(request):
   if(request.method=='POST'):
          student_id=request.POST.get('student_id')
          book_id=request.POST.get('book_id')
          loan_date=request.POST.get('loan_date')
          duration=request.POST.get('duration')
          student_instance = Student.objects.get(id_student=student_id)
          book_instance = Book.objects.get(id_book=book_id)
          new_loan=Loan(student_id=student_instance,book_id=book_instance,loan_date=loan_date,duration=duration)
          new_loan.save()
          return redirect("Loan")
   return render(request, 'loan.html')

def updateLoan(request,id):
     if(request.method=='POST'):
          student_id=request.POST.get('student_id')
          book_id=request.POST.get('book_id')
          loan_date=request.POST.get('loan_date')
          duration=request.POST.get('duration')
          student_instance = Student.objects.get(id_student=student_id)
          book_instance = Book.objects.get(id_book=book_id)
          new_loan=Loan(id_loan=id,student_id=student_instance,book_id=book_instance,loan_date=loan_date,duration=duration)
          new_loan.save()
          return redirect("Loan")
     return render(request, 'loan.html')

def deleteLoan(request,id):
     loan=Loan.objects.get(id_loan=id)
     loan.delete()
     return redirect("Loan")
     