from django import forms
from .models import  RoomData

class RoomDataForm(forms.ModelForm):
    class Meta:
        model = RoomData  
        fields = ['title','room_id','floor','bed','bathroom','location','about','desc','prize','wifi',
            'photo', 'updated_by'
        ]
