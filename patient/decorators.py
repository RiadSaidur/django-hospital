from django.shortcuts import redirect

def patient_only(view_func):
  def warpper_func(request, *args, **kwargs):
    group = ''
    if request.user.groups.exists():
      group = request.user.groups.all()[0].name
    if group == 'assistant':
      print(group)
      return redirect('assistant:index')
    else:
      return view_func(request, *args, **kwargs)
  return warpper_func