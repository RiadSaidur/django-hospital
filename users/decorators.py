from django.shortcuts import redirect

def only_unauthenticated(view_func):
  def warpper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('home')
    else:
      return view_func(request, *args, **kwargs)
  return warpper_func