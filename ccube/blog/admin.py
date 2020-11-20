from django.contrib import admin
from blog.models import Post, AssignCourses, SideBar, Quiz, Question, Response, quiztaker, userans
import nested_admin
admin.site.register(AssignCourses)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(Quiz)
class ResponseAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(quiztaker)
class ResponseAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)


@admin.register(userans)
class ResponseAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineInject.js',)
