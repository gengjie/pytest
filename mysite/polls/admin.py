__author__ = 'gengjie'
from models import Poll
from models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    # extra = 3

class PollAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields':['question']}),
    #     ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
    # ]
    list_display = ['question', 'pub_date', 'was_published_recently']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)