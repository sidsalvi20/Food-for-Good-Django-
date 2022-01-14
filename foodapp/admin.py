from django.contrib import admin

# Register your models here.

from .models import Food
from .models import Comment
from .models import Profile


admin.site.register(Comment)
admin.site.register(Food)
admin.site.register(Profile)



