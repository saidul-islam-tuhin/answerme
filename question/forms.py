from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write what you want to know', 'class': 'ask-input w-input'
                                            ,'id':'name','data-name':'Name','autofocus':True,'maxlength':256}))

    class Meta:
        fields = ['text']
