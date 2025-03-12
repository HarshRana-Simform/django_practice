from django.contrib import admin
from blog.models import Posts_db
# Register your models here.


# @admin.register(Posts_db)  To register with decortor rather than the admin.site.register method
class Posts_dbAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content',
                    'published_date', 'last_modified')


admin.site.register(Posts_db, Posts_dbAdmin)
