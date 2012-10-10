from forms import FormUser
from models import User
from django.shortcuts import render_to_response


def edit_user(request,user_id=None):

   if user_id:
      user = User.objects.get(id=user_id)
   else:
      user = None

   if request.method == request.POST:
      form = FormUser(request.POST, instance=user)

      if form.is_valid():
         user = form.save()

         if user:
            return HttpResponse('Usuario salvo com sucesso!')

   else:
      form = FormUser(instance=user)

   return render_to_response('register/edit_user.html',locals(),)


