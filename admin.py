
from django.contrib import admin
from .models import Question, Choice, Submission, Course, Lesson, Instructor, Learner

# Inline classes
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

# Admin classes
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'grade')
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [QuestionInline]

# Registering the models (assuming these models exist in your app)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)