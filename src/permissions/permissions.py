#constant lists to use as a parameter for permission_required decorator

ECOMMERCE_STAFF = ['products.add_product','products.change_product','products.delete_product','products.view_product','products.add_brand','products.change_brand','products.delete_brand','products.view_brand','shopping_cart.add_cart','shopping_cart.change_cart','shopping_cart.delete_cart','shopping_cart.view_cart']

ECOMMERCE_CLIENT = ['products.view_product','products.view_brand','shopping_cart.change_cart','shopping_cart.view_cart']
