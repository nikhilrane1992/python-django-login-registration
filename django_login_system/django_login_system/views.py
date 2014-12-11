from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib import auth
import json
from forms import AdminRegistrationForm
from django.contrib.auth.models import User


#------------------------------------------------------------------------------------------------------------------------
#                             Login System
#------------------------------------------------------------------------------------------------------------------------
def login(request):
    return render_to_response('login.html')


#------------------------------------------------------------------------------------------------------------------------
#                             Register New user using django Form
#------------------------------------------------------------------------------------------------------------------------
def register_user(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AdminRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                register_success = [{"validation" : "Registered Sucessfully", "status": True}]
                return HttpResponse(json.dumps(register_success), content_type = "application/json")

        args = {}
        args['form'] = AdminRegistrationForm()
        return render_to_response('register.html',args)
    else:
        models_data = [{"validation" : "authentication failure", "status": False}]
        return HttpResponse(json.dumps(models_data), content_type = "application/json")


#------------------------------------------------------------------------------------------------------------------------
#                             Login Auth for every user
#------------------------------------------------------------------------------------------------------------------------
def auth_view(request):
	if request.POST:
	    username = request.POST['username']
	    password = request.POST['password']

	    # username = request.POST.get('username', ' ')
	    # password = request.POST.get('password', ' ')
	    print username,password
	    # print dir(request)
	    user = auth.authenticate(username=username, password=password)

	    if user is not None:
			auth.login(request, user)
			Status = [{"validation": "Login Successful", "status": True}]
			return HttpResponse(json.dumps(Status), content_type="application/json")

	    else:
	        Status = [{"validation": "Authentication failure", "status": False}]
	        return HttpResponse(json.dumps(Status), content_type="application/json")
	else:
		return HttpResponse(json.dumps([{"validation": "I am watching you (0_0)", "status": False}]), content_type="application/json")



#------------------------------------------------------------------------------------------------------------------------
#                             Register new user using post request
#------------------------------------------------------------------------------------------------------------------------
def registerUser(request):
	# print request.POST
	if request.POST:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password1 = request.POST['password1']
		print username, email, password1, password
		user=User()
		user.username = username
		user.email = email
		if password == password1:
			user.set_password(password)
		else:
			return HttpResponse(json.dumps([{"validation": "Password does not match", "status": False}]), content_type="application/json")
		# user.is_staff = True
		user.save()
		register_success = [{"validation" : "Registration Successful", "status": True}]
		return HttpResponse(json.dumps(register_success), content_type="application/json")
	else:
		return HttpResponse(json.dumps([{"validation": "I am watching you (0_0)", "status": False}]), content_type="application/json")
