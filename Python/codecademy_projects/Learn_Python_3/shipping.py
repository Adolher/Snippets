weight = int(input("What's the weight of your package?"))


class Prices:
    def __init__(self, weight):
        self.shipping_methods = {"Ground Shipping": 20.0 + self.calc_shipping(weight, "gs"),
            "Premium Shipping": 125.0,
            "Drone Shipping": self.calc_shipping(weight, "ds"),
            }

    def calc_shipping(self, w, m):
        if w <= 2:
            return 1.5 * w if m == "gs" else 4.5 * w
        elif w <= 6:
            return 3.0 * w if m == "gs" else 9.0 * w
        elif w <= 10:
            return 4.0 * w if m == "gs" else 12.0 * w
        else:
            return 4.75 * w if m == "gs" else 14.25 * w

    def get_cheapest(self):
        x = min(self.shipping_methods.values())
        key = [k for k, v in self.shipping_methods.items() if v == x][0]
        return key, x

price = Prices(weight)


msg = "The cheapest shipping method is {} with {} $"
x = price.get_cheapest()
print(msg.format(x[0], x[1]))