from django import forms
from . import models, parser_jutsu

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('jutsu', 'jutsu'),
    )
    media_ytpe = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            "media_type"
        ]
    def parser_data(self):
        if self.data['media_type'] == 'jutsu':
            jutsu_file = parser_jutsu.parsing()
            for i in jutsu_file:
                models.JutsuModel.objects.create(**i)