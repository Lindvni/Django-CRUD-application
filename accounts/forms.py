from django import forms


class Mindforms(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="First Name")

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Last Name")

    position = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Position")

    company = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Company")

    startdate = forms.DateField(widget = forms.SelectDateWidget)
    enddate = forms.DateField(widget = forms.SelectDateWidget)

    duration = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Duration")

    pay_rate = forms.DecimalField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Pay Rate")

    bill_rate = forms.DecimalField(widget=forms.TextInput(attrs={
        "class": "input",
        "type" : "text",
    }), label ="Bill Rate")
    
    