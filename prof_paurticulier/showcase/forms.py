from django import forms

from authentication.models import SchoolSubject, Grade


class FilterShowcaseForm(forms.Form):
    interests = forms.ModelMultipleChoiceField(
        queryset=SchoolSubject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    grades = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        fields = ("interests", "grades")
