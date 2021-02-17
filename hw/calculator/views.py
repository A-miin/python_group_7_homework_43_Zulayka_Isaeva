from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def calculator(request):
    if request.method=="GET":
        return render(request, 'calculator_view.html')
    elif request.method=="POST":
        result = 0
        operation = ''
        first_number = float(request.POST.get('first_number'))
        second_number = float(request.POST.get('second_number'))

        if request.POST.get('operation')=='add':
            result = first_number+second_number
            operation = '+'
        elif request.POST.get('operation')=='subtract':
            result = first_number - second_number
            operation = '-'
        elif request.POST.get('operation')=='multiply':
            result = first_number * second_number
            operation = '*'
        elif request.POST.get('operation')=='divide':
            if second_number==0:
                return render(request,'calculator_view.html',{'error':True})
            result = first_number / second_number
            operation = '/'

        context = {
            'first_number':first_number,
            'second_number': second_number,
            'operation': operation,
            'result': result,
        }
        return render(request, 'calc_result.html', context)
