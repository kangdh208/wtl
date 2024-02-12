from django.shortcuts import render, redirect
from .forms import LeadForm

def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_success')  # Redirect to success page
    else:
        form = LeadForm()
    return render(request, 'leads/lead_form.html', {'form': form})