from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # ou admin.StackedInline
    model = Choice  # Aqui você define o modelo
    extra = 3  # Número de opções extras a serem exibidas

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # Adiciona as opções como inline

admin.site.register(Question, QuestionAdmin)