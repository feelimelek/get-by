from rest_framework import viewsets
from .models import Address
from .models import Emotion
from .models import Tip
from .models import Comment
from .models import EmotionTip
from .models import Person
from .models import PersonEmotion
from .models import Selection
from .models import Task
from .serializers import AddressSerializer
from .serializers import EmotionSerializer
from .serializers import TipSerializer
from .serializers import CommentSerializer
from .serializers import EmotionTipSerializer
from .serializers import PersonSerializer
from .serializers import PersonEmotionSerializer
from .serializers import SelectionSerializer
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cep', 'state']

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer

class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class EmotionTipViewSet(viewsets.ModelViewSet):
    queryset = EmotionTip.objects.all()
    serializer_class = EmotionTipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emotion_id', 'tip_id']

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonEmotionViewSet(viewsets.ModelViewSet):
    queryset = PersonEmotion.objects.all()
    serializer_class = PersonEmotionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['person_id', 'emotion_id']

class SelectionViewSet(viewsets.ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
