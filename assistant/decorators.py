from django.shortcuts import redirect

def assistant_only(view_func):
  def warpper_func(request, *args, **kwargs):
    group = ''
    if request.user.groups.exists():
      group = request.user.groups.all()[0].name
    if group == 'patient':
      print(group)
      return redirect('home')
    else:
      return view_func(request, *args, **kwargs)
  return warpper_func