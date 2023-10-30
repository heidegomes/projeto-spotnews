from django import forms
from news.models import News, Category, User


class CreateNewModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        # self.fields["content"].widget = forms.Textarea()
        self.fields["author"].label = "Autoria"
        self.fields["author"].widget = forms.SelectMultiple()
        self.fields["author"].queryset = User.objects
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da imagem"
        # self.fields["image"].widget = forms.FileInput()
        self.fields["categories"].widget = forms.CheckboxSelectMultiple()
        self.fields["categories"].queryset = Category.objects.all()


class CreateCategorieModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
