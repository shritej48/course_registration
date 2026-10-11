from django.db import models


class course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.IntegerField()

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name


class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    ph = models.CharField(max_length=15)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.student_name


class enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return f"{self.student_name} → {self.course_name}"