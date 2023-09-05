from django.db import models

class Pizza(models.Model):
    base_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    extra_cheese_added = models.BooleanField(default=False)
    extra_toppings_added = models.BooleanField(default=False)

    def add_extra_cheese(self):
        if not self.extra_cheese_added:
            self.base_price += 80
            self.extra_cheese_added = True

    def add_extra_toppings(self):
        if not self.extra_toppings_added:
            if isinstance(self, DeluxePizza):
                self.base_price += 120
            else:
                self.base_price += 70
            self.extra_toppings_added = True

    def add_paperbag(self):
        self.base_price += 20

    def generate_bill(self):
        bill = f"Base Price Of The Pizza: {self.base_price}\n"
        
        if self.extra_cheese_added:
            bill += f"Extra Cheese Added: 80\n"

        if self.extra_toppings_added:
            if isinstance(self, DeluxePizza):
                bill += f"Extra Toppings Added: 120\n"
            else:
                bill += f"Extra Toppings Added: 70\n"

        return bill

class DeluxePizza(Pizza):
    pass
