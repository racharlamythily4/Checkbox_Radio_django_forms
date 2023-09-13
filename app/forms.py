from django import forms

ch=[('male','MALE'),('female','FEMALE')]
cr=[('python','PYTHON'),('Django','django'),('api','API')]
class Student(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField()
    Semail=forms.EmailField()
    Remail=forms.EmailField()
    Passward=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Gender=forms.ChoiceField(choices=ch)
    #Gender=forms.ChoiceField(choices=ch,widget=forms.RadioSelect)
    #Course=forms.MultipleChoiceField(choices=cr)
    Course=forms.MultipleChoiceField(choices=cr,widget=forms.CheckboxSelectMultiple)

