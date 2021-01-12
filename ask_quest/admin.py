from django.contrib import admin

from .models import Question, Chapter, Response

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('responsed'),
        


admin.site.register(Chapter)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
