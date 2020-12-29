from django.contrib import admin

from homepage.models import Project, Experience, Skill, Admin, Description, About


class DescripInLine(admin.StackedInline):
    model = Description
    extra = 3


class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [('Experience Info', {'fields': [
                  'exp_type', 'company_name', 'location', 'position', 'duration'], 'classes':['colapse']})]

    inlines = [DescripInLine]


admin.site.register(Project)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill)
admin.site.register(Admin)
admin.site.register(About)
