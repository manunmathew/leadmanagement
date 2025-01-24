from django.shortcuts import render,redirect
from django.views.generic import View
from leadmanagement_app.models import Lead
from leadmanagement_app.forms import LeadForm
from django.db.models import Count

# Create your views here.

class LeadCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=LeadForm()
        return render(request, "lead_create.html",{"form": form_instance})
    
    def post(self, request, *args, **kwargs):
        form_data=request.POST
        form_instance=LeadForm(form_data)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("lead_list")
        return render(request, "lead_create.html",{"form": form_instance})
    

class LeadListView(View):
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        return render(request, "lead_list.html", {"leads": leads})
    

class LeadUpdateView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        lead_object = Lead.objects.get(id=id)
        form_instance = LeadForm(instance=lead_object)
        return render(request, "lead_update.html", {"form": form_instance})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        lead_object = Lead.objects.get(id=id)
        form_data = request.POST
        form_instance = LeadForm(form_data, instance=lead_object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("lead_list")
        return render(request, "lead_update.html", {"form": form_instance})

class LeadDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Lead.objects.get(id=id).delete()
        return redirect("lead_list")

class LeadSummaryView(View):
    def get(self, request, *args, **kwargs):
        total_leads = Lead.objects.aggregate(total=Count("id"))
        status_summary = Lead.objects.values("status").annotate(count=Count("status")) 
        context = {
            "total_leads": total_leads["total"],
            "status_summary": status_summary,
        }
        return render(request, "lead_summary.html", context)