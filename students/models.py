from django.db import models

class Student(models.Model):  # Capitalized model name
    student_id = models.CharField(max_length=10, unique=True)  # Unique constraint
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id} - {self.name}"
