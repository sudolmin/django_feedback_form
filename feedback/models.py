from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Form(models.Model):
    Recipient = models.OneToOneField(User,
                     on_delete=models.CASCADE,
                     help_text=("User who will recieve feedback."))
    title = models.CharField(max_length=50)
    form_slug_url = models.SlugField(
        max_length=60, blank=False,
        help_text=("a user non-friendly url"),
        verbose_name=("user non-friendly url"))

    def __str__(self):
        return self.Recipient.username

class Questions(models.Model):
    forms = models.ForeignKey(Form,
                                    verbose_name=("Forms"),
                                    blank=False,
                                    on_delete=models.CASCADE)
    Question = models.CharField(
		verbose_name=("Question"),
		max_length=100)

    def __str__(self):
        return self.Question

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Question = models.ForeignKey(Questions,
                                    verbose_name=("Question"),
                                    blank=False,
                                    on_delete=models.CASCADE)
    Descibe = models.TextField(max_length=200,
                                 blank=False,
                                 help_text=("Explanation to be shown "
                                             "after the question has "
                                             "been answered."),
                                 verbose_name=('Add Comment'))
    Rate = models.IntegerField(default = 5, blank=False,
								help_text=("""Please Rate out of 10 in support of your answer"""),
                            	verbose_name=('Rate(out of 10)'),
                            	validators=[MaxValueValidator(10), MinValueValidator(0)])
    def __str__(self):
        return self.author.username