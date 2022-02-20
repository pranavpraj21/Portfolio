from django import forms
from .models import reviewed

CHOICES =(
    ("⭐", "1/5"),
    ("⭐⭐", "2/5"),
    ("⭐⭐⭐", "3/5"),
    ("⭐⭐⭐⭐", "4/5"),
    ("⭐⭐⭐⭐⭐", "5/5"),
)
class reviewform(forms.ModelForm):
    Rating = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model=reviewed
        fields=['Relationship','Description','Rating','Social']

        widgets = {
        'Relationship': forms.TextInput(attrs={'class':'form-control'}),
        'Description': forms.Textarea(attrs={'class':'form-control'}),
        #'Rating': forms.Select(attrs={'class':'form-control'}),
        'Social': forms.TextInput(attrs={'class':'form-control'}),
        }
