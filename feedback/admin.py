from django.contrib import admin
from .models import Form, Questions, Answer
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('Question', 'author', 'Descibe', 'Rate')

class QuestionInline(admin.TabularInline):
    model = Questions

class FormsAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]

admin.site.register(Form, FormsAdmin)
admin.site.register(Answer, AnswerAdmin)
