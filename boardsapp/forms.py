# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:12:22 2020

@author: 1332954
"""
from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
