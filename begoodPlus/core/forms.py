


from django import forms

from .models import BeseContactInformation

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

class FormBeseContactInformation(BaseForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'שם'}), label='', )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'אימייל'}), label='',)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'פאלפון'}), label='',)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'הודעה', 'rows':'2'}), label='', )
    class Meta:
        model = BeseContactInformation
        fields = '__all__'