from django.shortcuts import render
from django.http import HttpResponse
from servies.models import Servies


def index(request):
    serviesData=Servies.objects.all()
    data ={
        'serviesData':serviesData
    }
    return render(request,'index.html',data)






# def index(request):
    
#     if request.method == 'POST':
#         n1 = float(request.POST['num1'])
#         n2 = float(request.POST['num2'])
#         operation = request.POST['operation']

#         if operation == 'add':
#             result = n1 + n2
#         elif operation == 'subtract':
#             result = n1 - n2
#         elif operation == 'multiply':
#             result = n1 * n2
#         elif operation == 'divide':
#             if n2 == 0:
#                 result = "Error: Division by zero"
#             else:
#                 result = n1 / n2
#         else:
#             result = "Invalid operation"

#         return render(request, 'index.html', {'result': result})
#     else:
#         return render(request, 'index.html')
    
# # def about(request):
#     result = 0
#     data ={}
#     if request.method == 'POST':
#         a1= float(request.POST['num1'])
#         a2= float(request.POST['num2'])
#         op = request.POST['operation']
        
#         if op == 'add':
#             result = a1+a2
#         elif op == 'subtract':
#             result = a1-a2
#         elif op == 'multiply':
#             result = a1*a2
#         elif op == 'divide':
#             if a2 == 0:
#                 result = "error:diviser is not zero"
#             else:
#                 result = a1/a2
#         else:
#             result = "Invalide syntex"
#         data ={'result':result}
#         print(result)
#         return render(request,'about.html',data)
#     else:
#         return render(request, 'index.html')

# def about(request):
#     result =''
#     try:
#         if request.method == 'POST':
#             num = eval(request.POST['num1'])
#             if num%2 == 0:
#                 result = "Evan number"
#             else:
#                 result = "Odd number"
#     except :
#         result = "value error pleas enter integer"
#     return render(request, 'about.html',{'result' : result})

