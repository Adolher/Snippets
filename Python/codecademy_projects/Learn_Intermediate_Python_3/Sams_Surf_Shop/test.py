import unittest

import surfshop

class SurfShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.shopping_cart = surfshop.ShoppingCart()

    def test_add_surfboards_OK(self) -> None:
        for num in [1, 2, 3, 4, 5, 6]:
            self.setUp()
            with self.subTest(num):
                pre = "s" if num != 1 else ""
                exp_result = f"Successfully added {num} surfboard{pre} to cart!"
                if num <= 4:
                    self.assertEqual(self.shopping_cart.add_surfboards(num), exp_result)
                elif num > 4:
                    #self.skipTest("Out of season")
                    self.assertRaises(surfshop.TooManyBoardsError, self.shopping_cart.add_surfboards, num)

#    @unittest.expectedFailure
    def test_local_discount(self) -> None:
        self.shopping_cart.apply_locals_discount()
        self.assertTrue(self.shopping_cart.locals_discount)

unittest.main()