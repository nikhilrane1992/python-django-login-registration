from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib import auth
import json
from forms import AdminRegistrationForm


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
                register_success = [{"registration" : "Register Sucessfully" }]
                return HttpResponse(json.dumps(register_success), content_type = "application/json")

        args = {}
        args['form'] = AdminRegistrationForm()
        return render_to_response('register.html',args)
    else:
        models_data = [{"status" : "authentication failure"}]
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
			Status = [{"status": "Login Successfully"}]
			return HttpResponse(json.dumps(Status), content_type="application/json")

	    else:
	        Status = [{"status": "Authentication failure"}]
	        return HttpResponse(json.dumps(Status), content_type="application/json")
	else:
		return HttpResponse(json.dumps([{"validation": "I am watching you (0_0)", "status": False}]), content_type="application/json")



#------------------------------------------------------------------------------------------------------------------------
#                             Register new user using post request
#------------------------------------------------------------------------------------------------------------------------
def registerUser(request):
    if request.POST:
        dataDictionary = json.loads(request.body)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        user=User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password == password1:
            user.set_password(password)
        else:
            return HttpResponse(json.dumps([{"validation": "Password does not match", "status": False}]), content_type="application/json")
        # user.is_staff = True
        user.save()
        register_success = [{"validation" : "Register Successfully", "status": True}]
        return HttpResponse(json.dumps(register_success), content_type="application/json")
    else:
        return HttpResponse(json.dumps([{"validation": "I am watching you (0_0)", "status": False}]), content_type="application/json")
