from django.http import HttpResponse

def PermissionVerify(function):
    def wrapper(request, *args, **kwargs):
        userid = request.user.myuser.id
        if request.path != "/User_Management/user_info/"+str(userid)+"/":
            return HttpResponse('You cannot view this.')
        else:
            return function(request, *args, **kwargs)
    return wrapper