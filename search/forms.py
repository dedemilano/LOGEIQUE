from django import forms 

class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length= 200, widget=forms.TextInput(attrs={'id':'query', 'class':'form-control mr-sm-2', 'title':'Rechercher', 'placeholder':'exemple : Marcory...' , 'aria-label':"Search"}))
    query_for_all= forms.BooleanField(label='Tout', required=False, widget=forms.CheckboxInput(attrs={'id':'tout', 'checked':'checked'}))
    query_for_house = forms.BooleanField(label='Maison', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'hou'}))
    query_for_client = forms.BooleanField(label='Client', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'cli'}))
    query_for_lanlord = forms.BooleanField(label='Propietaire', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'lan'}))
