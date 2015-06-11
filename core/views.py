from django.shortcuts import render 
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView
from sitegate.decorators import redirect_signedin, sitegate_view 
import core.models as coremodels
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import ContactForm
from django.template import RequestContext, Context
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.template.context_processors import csrf



class LandingView(TemplateView):
    template_name = 'base/index.html'

class LocationListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'
    paginate_by = 5

class SearchListView(LocationListView):
	
	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query','')
		return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = 'location/detail.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        location = coremodels.Location.objects.get(id=self.kwargs['pk'])
        if self.request.user.is_authenticated():
            user_reviews = coremodels.Review.objects.filter(location=location, user=self.request.user)
            if user_reviews.count() > 0:
                context['user_review'] = user_reviews[0]
            else:
                context['user_review'] = None

        return context

class LocationCreateView(CreateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"

class LocationUpdateView(UpdateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['description' , 'rating']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.location = coremodels.Location.objects.get(id = self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.location.get_absolute_url()

class ReviewUpdateView(UpdateView):
    model = coremodels.Review
    template_name = 'base/form.html'
    fields =['description', 'rating',]

    def get_object(self):
        return coremodels.Review.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

def contactview(request):
        subject = request.POST.get('topic', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        c = {}
        c.update(csrf(request))

        if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['team@turfwork.co'])
                except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/thankyou/')
        else:
            return render_to_response('base/form.html', {'form': ContactForm()},RequestContext(request))
    
        return render_to_response('base/form.html', {'form': ContactForm()},
            RequestContext(request))

def thankyou(request):
        return render_to_response('templates/base/thankyou.html')

    

