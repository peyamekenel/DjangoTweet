from django.contrib import admin
from tweetapp.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    #fields = ["message","nickname"]
    fieldsets=[
        ("Message Group",{"fields":["message"]}),
        ("NickName Group",{"fields":["nickname"]})
    ]
admin.site.register(Tweet,TweetAdmin)