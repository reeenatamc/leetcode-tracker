from django.db import models

# Create your models here.

class status(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    def __str__(self):
        return self.name

class problem(models.Model):
    DIFFICULTY_EASY = 'Easy'
    DIFFICULTY_MEDIUM = 'Medium'
    DIFFICULTY_HARD = 'Hard'

    DIFFICULTY_CHOICES = (
        (DIFFICULTY_EASY, 'Easy'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_HARD, 'Hard'),
    )

    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    acceptance_level = models.FloatField()
    status = models.ForeignKey(status, on_delete=models.CASCADE)

class solution(models.Model):
    problem = models.ForeignKey(problem, on_delete=models.CASCADE)
    lang_name = models.CharField(max_length=100)
    observations = models.TextField()
    date_solved = models.DateTimeField(auto_now_add=True)
    time_spent_on = models.IntegerField(auto_now=True)
    link_code = models.TextField()
    code_version = models.IntegerField()
    runtime = models.FloatField()
    memory = models.FloatField()


    def __str__(self):
        return self.problem.name

class streak(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    compliance_percentage = models.FloatField()
    def __str__(self):
        return self.name

class streak_registered(models.Model):
    streak = models.ForeignKey(streak, on_delete=models.CASCADE)
    streak_date = models.DateTimeField(auto_now_add=True)
    compliance = models.BooleanField()
    is_the_record_still_a_streak = models.BooleanField()
    def __str__(self):
        return self.streak.name