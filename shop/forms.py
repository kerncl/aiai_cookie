from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1,11)],
        coerce=int
    )
