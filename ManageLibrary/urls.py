"""
URL configuration for ManageLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views
urlpatterns = [
    path("admin/", admin.site.urls,name="Admin"),
    path("", views.student, name="Student"),
    path("Student/", views.student,name="Student"), 
    path("AddStudent/", views.addStudent,name="AddStudent"),
    path("UpdateStudent/<int:id>", views.updateStudent,name="UpdateStudent"),
    path("DeleteStudent/<int:id>", views.deleteStudent,name="DeleteStudent"),
    
    path("Book/", views.book,name="Book"), 
    path("AddBook/", views.addBook,name="AddBook"),
    path("UpdateBook/<int:id>", views.updateBook,name="UpdateBook"),
    path("DeleteBook/<int:id>", views.deleteBook,name="DeleteBook"),
    
    path("Loan/", views.loan,name="Loan"), 
    path("AddLoan/", views.addLoan,name="AddLoan"),
    path("UpdateLoan/<int:id>", views.updateLoan,name="UpdateLoan"),
    path("DeleteLoan/<int:id>", views.deleteLoan,name="DeleteLoan")
]

