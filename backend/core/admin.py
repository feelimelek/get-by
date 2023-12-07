from django.contrib import admin
from .models import Address
from .models import Emotion
from .models import Comment
from .models import EmotionTip
from .models import Person
from .models import PersonEmotion
from .models import Selection
from .models import Task
from .models import Tip

admin.site.register(Address)
admin.site.register(Emotion)
admin.site.register(Comment)
admin.site.register(EmotionTip)
admin.site.register(Person)
admin.site.register(PersonEmotion)
admin.site.register(Selection)
admin.site.register(Task)
admin.site.register(Tip)