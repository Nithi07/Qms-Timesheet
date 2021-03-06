from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from QMS.models import EmployeeDetails
from QMS.form.empdetailsform import EmployeeDetailsform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy



#EmployeeDetails ListView
class EmployeeDetailsListview(ListView):
    model = EmployeeDetails
    template_name = 'superadmin/empdetails_view.html'

    def get_context_data(self, **kwargs):
        empdetails = self.model.objects.all().order_by('pk')
        obj = {'empdetails':empdetails}
        return obj



#EmployeeDetails CreateView
class EmployeeDetailsCreate(CreateView):
    model = EmployeeDetails
    form_class = EmployeeDetailsform
    success_url = 'QMS:empdetailsview'
    template_name = 'superadmin/empdetails_form.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailsCreate, self).get_context_data(**kwargs)
        context["form"] = EmployeeDetailsform()
        return context

    def get_success_url(self):
       return reverse_lazy(self.success_url)

    def post(self, request, *args, **kwargs):
        form = EmployeeDetailsform(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            emp_name = form.cleaned_data['emp_name']
            name_code  = form.cleaned_data['emp_name'],'-',form.cleaned_data['emp_code']
            new.emp_name = ''.join(name_code)
            new.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

#EmployeeDetails UpdateView
class EmployeeDetailsUpdate(UpdateView):
     model = EmployeeDetails
     form_class = EmployeeDetailsform
     success_url = 'QMS:empdetailsview'
     template_name = 'superadmin/empdetails_form.html'

     def get_success_url(self):
        return reverse_lazy(self.success_url)

     def form_valid(self, form):
        form = self.get_form()
        form.save()
        return HttpResponseRedirect(self.get_success_url())

#EmployeeDetails DeleteView
class EmployeeDetailsDelete(DeleteView):
    model = EmployeeDetails
    success_url = 'QMS:empdetailsview'
    template_name = 'superadmin/empdetails_confirm_delete.html'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EmployeeDetailsDelete, self).get_object()
        return obj
    def get_success_url(self):
        return reverse_lazy(self.success_url)
