from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_avg_grade(self):
        try:
            return sum(grade.value for grade in self.grade_set.all()) / self.grade_set.all().count()
        except ZeroDivisionError:
            return ''

    @property
    def get_grade_list(self):
        return [grade.value for grade in self.grade_set.all()]


class Recruiter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Grade(models.Model):
    F = 1
    E = 2
    D = 3
    C = 4
    B = 5
    A = 6
    RATE_CHOICES = (
        (F, 1),
        (E, 2),
        (D, 3),
        (C, 4),
        (B, 5),
        (A, 6)
    )
    value = models.IntegerField(choices=RATE_CHOICES)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
