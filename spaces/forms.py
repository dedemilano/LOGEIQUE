from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Pseudo : ', max_length=200, widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Pseudo', 'placeholder': 'Entrez votre pseudo'}))
    first_name = forms.CharField(label='Prenom : ', max_length=200, widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Prenom', 'placeholder': 'Entrez votre Prenom'}))
    last_name = forms.CharField(label='Nom', max_length=200, widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Nom', 'placeholder': 'Entrez votre Nom'}))
    email = forms.EmailField(label='Email : ', required=False, widget=forms.EmailInput(
        attrs={'class': 'inbox', 'title': 'Email', 'placeholder': 'Entrez votre addresse electronique', 'id': 'lo_em'}))
    contact = forms.CharField(label='Contact : ', widget=forms.TextInput(
        attrs={'class': 'inbox', 'title': 'Contact', 'placeholder': 'Exemple : 00-00-00-00', 'id': 'lo_nu'}))
    client = forms.BooleanField(label='Client : ', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'stick', 'onclick': 'active()', 'id': 'is_cl'}))
    landlord = forms.BooleanField(label='Proprietaire : ', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'stick', 'onclick': 'active()', 'id': 'is_la'}))
    password = forms.CharField(label='Mot de passe :', max_length=200, widget=forms.PasswordInput(attrs={
        'class': 'inbox', 'title': 'Mot de passe', 'placeholder': 'Entrez votre mot de passe'}))
    password_verification = forms.CharField(label='Vérification', max_length=200, widget=forms.PasswordInput(attrs={
        'class': 'inbox', 'title': 'Vérification', 'placeholder': 'Entrez votre mot de passe à nouveau'}))


class SignInForm(SignUpForm):
    first_name = None
    last_name = None
    email = None
    contact = None
    password_verification = None


class EditForm(forms.Form):
    username = forms.CharField(label='Pseudo : ', max_length=200, required=False , widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Pseudo', 'placeholder': 'Entrez votre pseudo'}))
    first_name = forms.CharField(label='Prenom : ', max_length=200, required=False ,widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Prenom', 'placeholder': 'Entrez votre Prenom'}))
    last_name = forms.CharField(label='Nom', max_length=200, required=False ,widget=forms.TextInput(attrs={
        'class': 'inbox', 'title': 'Nom', 'placeholder': 'Entrez votre Nom'}))
    email = forms.EmailField(label='Email : ', required=False, widget=forms.EmailInput(attrs={'class': 'inbox', 'title': 'Email', 'placeholder': 'Entrez votre addresse electronique', 'id': 'lo_em'}))
    contact = forms.CharField(label='Contact : ',required=False , widget=forms.TextInput(attrs={'class': 'inbox', 'title': 'Contact', 'placeholder': 'Exemple : + 225 00-00-00-00', 'id': 'lo_nu'}))
    password = forms.CharField(label='Mot de passe :',required=False ,  max_length=200, widget=forms.PasswordInput(attrs={'class': 'inbox', 'title': 'Mot de passe', 'placeholder': 'Entrez votre mot de passe'}))
    password_verification = forms.CharField(label='Vérification', required=False, max_length=200, widget=forms.PasswordInput(attrs={'class': 'inbox', 'title': 'Vérification', 'placeholder': 'Entrez votre mot de passe à nouveau'}))


class AddHouseForm(forms.Form):
    house_area = forms.CharField(max_length=50)
    house_rent = forms.IntegerField()
    house_deposit = forms.IntegerField()
    house_kind = forms.CharField(max_length=50)
    house_rooms_number = forms.IntegerField()
    house_available = forms.BooleanField()
    house_to_sell = forms.BooleanField()
    house_image = forms.ImageField(upload_to="houses/")
