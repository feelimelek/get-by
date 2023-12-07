from rest_framework import serializers
from .models import Address
from .models import Emotion
from .models import Comment
from .models import EmotionTip
from .models import Person
from .models import PersonEmotion
from .models import Selection
from .models import Task
from .models import Tip

class AddressSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Address
        fields = ['cep', 'state', 'streetname', 'city']

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Emotion
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Comment
        fields = ['id', 'senderid', 'istipcreator', 'datetime', 'text', 'tip_id']

class EmotionTipSerializer(serializers.ModelSerializer):
    class Meta:        
        model = EmotionTip
        fields = ['emotion_id', 'tip_id']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'points', 'password', \
                  'specializationfield', 'professional_id', 'phonenumber', 'isadmin']
    
class PersonEmotionSerializer(serializers.ModelSerializer):
    class Meta:        
        model = PersonEmotion
        fields = ['person_id', 'emotion_id']

class SelectionSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Selection
        fields = ['id', 'person_id', 'tip_id', 'task_id', 'emotion_id', 'datetime', 'has_helped']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Task
        fields = ['id', 'description', 'duedate', 'completed', 'emotion_id', 'tip_id']


class TipSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Tip
        fields = ['id', 'name', 'description', 'points', 'cep', 'state', \
                  'buildingnumber', 'complement', 'country', 'validated', 'tip_creator_id']

  