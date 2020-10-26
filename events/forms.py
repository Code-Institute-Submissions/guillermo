from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    # In order to display a date and time pickers in the form
    date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    time = forms.TimeField(widget=forms.TextInput(attrs={"type": "time"}))
    # To pre-populate
    event_url = forms.URLField(initial='https://', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"