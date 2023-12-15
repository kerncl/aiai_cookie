from .cart import Cart


# Create context that all app able to access it & html can access it
def cart(request):
    return {'cart': Cart(request)}
