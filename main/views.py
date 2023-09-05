from django.shortcuts import render
from .models import Pizza, DeluxePizza

def pizza_bill_generator(request):
    context = {}
    if request.method == 'POST':
        pizza_type = request.POST.get('pizza_type', 'regular')
        veg = request.POST.get('veg', 'false')
        extra_cheese = request.POST.get('extra_cheese', 'false')
        extra_toppings = request.POST.get('extra_toppings', 'false')
        takeaway = request.POST.get('takeaway', 'false')

        if pizza_type == 'regular':
            pizza = Pizza(base_price=300)
        else:
            pizza = DeluxePizza(base_price=400)

        if veg == 'true':
            pizza.add_extra_toppings()

        if extra_cheese == 'true':
            pizza.add_extra_cheese()

        if extra_toppings == 'true':
            pizza.add_extra_toppings()

        if takeaway == 'true':
            pizza.add_paperbag()

        bill = pizza.generate_bill()
        context['bill'] = bill

    return render(request, 'pizza_bill.html', context)
