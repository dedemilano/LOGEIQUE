from django import forms 

class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length= 200, widget=forms.TextInput(attrs={'id':'query', 'class':'search-bar', 'title':'Rechercher', 'placeholder':'exemple : Marcory...'}))
    query_for_all= forms.BooleanField(label='Tout', required=False, widget=forms.CheckboxInput(attrs={'id':'tout', 'checked':'checked'}))
    query_for_house = forms.BooleanField(label='Canal+', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'hou'}))
    query_for_client = forms.BooleanField(label='Startimes', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'cli'}))
    query_for_lanlord = forms.BooleanField(label='Tnt', required=False, widget=forms.CheckboxInput(attrs={'class':'stick', 'onclick':'active()', 'id':'lan'}))
