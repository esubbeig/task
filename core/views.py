from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages

from .forms import DataCreationForm
from .models import *

# Class based view to handle add data form
class AddDataView(View):
    
    def get(self,request):
        form = DataCreationForm()
        category_list = Category.objects.all()
        return render(request, 'home.html', {'form': form, 'category_list' : category_list})

    def post(self, request):
        form = DataCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully!")
            return redirect('add_data')

        return render(request, 'home.html', {'form': form})

# AJAX to update the sub-category dropdown
class LoadSubcategory(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        try:
            subcategory = SubCategory.objects.filter(category_id=category_id).all()
        except SubCategory.DoesNotExist:
            subcategory = None
        return render(request, 'subcategory_dropdown.html', {'subcategory': subcategory})

