from .models import ProductReview
from django import forms


class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('title', 'review')