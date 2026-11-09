from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, StoreForm, ProductForm
from .models import Store, Product, Order, OrderItem, Review
from django.db import transaction



def register(request):
    """
    Handles registration of vendors and buyers.
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(
        request,
        'ecommerce/register.html',
        {'form': form}
    )


@login_required
def dashboard(request):
    """
    Displays the dashboard according to the user's role.
    """

    return render(
        request,
        'ecommerce/dashboard.html',
        {'user': request.user}
    )
# Create your views here.


@login_required
def store_list(request):
    """
    Displays stores belonging to the logged-in vendor.
    """

    if request.user.role != 'vendor':
        return redirect('dashboard')

    stores = Store.objects.filter(vendor=request.user)

    return render(
        request,
        'ecommerce/store_list.html',
        {'stores': stores}
    )


@login_required
def store_create(request):
    """
    Allows a vendor to create a store.
    """

    if request.user.role != 'vendor':
        return redirect('dashboard')

    if request.method == 'POST':
        form = StoreForm(request.POST)

        if form.is_valid():
            store = form.save(commit=False)
            store.vendor = request.user
            store.save()
            return redirect('store_list')

    else:
        form = StoreForm()

    return render(
        request,
        'ecommerce/store_form.html',
        {'form': form}
    )


@login_required
def store_update(request, pk):
    """
    Allows a vendor to update their own store.
    """

    if request.user.role != 'vendor':
        return redirect('dashboard')

    store = get_object_or_404(
        Store,
        pk=pk,
        vendor=request.user
    )

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)

        if form.is_valid():
            form.save()
            return redirect('store_list')

    else:
        form = StoreForm(instance=store)

    return render(
        request,
        'ecommerce/store_form.html',
        {'form': form}
    )


@login_required
def store_delete(request, pk):
    """
    Allows a vendor to delete their own store.
    """

    if request.user.role != 'vendor':
        return redirect('dashboard')

    store = get_object_or_404(
        Store,
        pk=pk,
        vendor=request.user
    )

    if request.method == 'POST':
        store.delete()
        return redirect('store_list')

    return render(
        request,
        'ecommerce/store_confirm_delete.html',
        {'store': store}
    )


@login_required
def product_list(request, store_pk):
    """Displays products belonging to a vendor's store."""

    if request.user.role != 'vendor':
        return redirect('dashboard')

    store = get_object_or_404(
        Store,
        pk=store_pk,
        vendor=request.user
    )

    products = Product.objects.filter(store=store)

    return render(
        request,
        'ecommerce/product_list.html',
        {'store': store, 'products': products}
    )


@login_required
def product_create(request, store_pk):
    """Allows a vendor to add a product to their store."""

    if request.user.role != 'vendor':
        return redirect('dashboard')

    store = get_object_or_404(
        Store,
        pk=store_pk,
        vendor=request.user
    )

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('product_list', store_pk=store.pk)
    else:
        form = ProductForm()

    return render(
        request,
        'ecommerce/product_form.html',
        {'form': form, 'store': store}
    )


@login_required
def product_update(request, pk):
    """Allows a vendor to edit their own product."""

    if request.user.role != 'vendor':
        return redirect('dashboard')

    product = get_object_or_404(
        Product,
        pk=pk,
        store__vendor=request.user
    )

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect(
                'product_list',
                store_pk=product.store.pk
            )
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'ecommerce/product_form.html',
        {'form': form, 'store': product.store}
    )


@login_required
def product_delete(request, pk):
    """Allows a vendor to delete their own product."""

    if request.user.role != 'vendor':
        return redirect('dashboard')

    product = get_object_or_404(
        Product,
        pk=pk,
        store__vendor=request.user
    )

    if request.method == 'POST':
        store_pk = product.store.pk
        product.delete()
        return redirect('product_list', store_pk=store_pk)

    return render(
        request,
        'ecommerce/product_confirm_delete.html',
        {'product': product}
    )


@login_required
def product_catalogue(request):
    """
    Displays products from all vendors' stores to buyers.
    """

    if request.user.role != 'buyer':
        return redirect('dashboard')

    products = Product.objects.select_related(
        'store',
        'store__vendor'
    ).all()

    return render(
        request,
        'ecommerce/product_catalogue.html',
        {'products': products}
    )


@login_required
def cart_view(request):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(
        request,
        'ecommerce/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
@require_POST
def add_to_cart(request, product_id):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    product = get_object_or_404(Product, pk=product_id)

    if product.quantity_available < 1:
        messages.error(request, 'This product is out of stock.')
        return redirect('product_catalogue')

    cart = request.session.get('cart', {})
    product_id = str(product.id)
    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.quantity_available:
        cart[product_id] = current_quantity + 1
        request.session['cart'] = cart
        messages.success(request, 'Product added to cart.')
    else:
        messages.error(request, 'Available stock limit reached.')

    return redirect('product_catalogue')


@login_required
@require_POST
def remove_from_cart(request, product_id):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart

    return redirect('cart_view')


@login_required
@require_POST
def checkout(request):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, 'Your shopping cart is empty.')
        return redirect('cart_view')

    try:
        with transaction.atomic():
            order = Order.objects.create(
                buyer=request.user,
                status='completed'
            )

            total = 0

            for product_id, quantity in cart.items():
                product = get_object_or_404(
                    Product.objects.select_for_update(),
                    pk=product_id
                )

                if quantity < 1 or product.quantity_available < quantity:
                    raise ValueError(
                        f'Insufficient stock for {product.name}.'
                    )

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product.name,
                    quantity=quantity,
                    unit_price=product.price
                )

                total += product.price * quantity

                product.quantity_available -= quantity
                product.save(
                    update_fields=['quantity_available']
                )

            order.total_amount = total
            order.save(update_fields=['total_amount'])

        request.session['cart'] = {}

        invoice_lines = [
            f"Order number: {order.id}",
            f"Buyer: {request.user.username}",
            "",
            "Purchased products:"
        ]

        for item in order.items.all():
            invoice_lines.append(
                f"{item.product_name} - "
                f"Quantity: {item.quantity}- "
                f"Unit price: R{item.unit_price}"
            )

        invoice_lines.append("")
        invoice_lines.append(
            f"Total amount: R{order.total_amount}"
        )

        if request.user.email:
            send_mail(
                subject=f"Invoice for Order #{order.id}",
                message="\n".join(invoice_lines),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True
            )

        messages.success(
            request,
            'Your order was placed successfully.'
        )

        return redirect(
            'order_success',
            order_id=order.id)

    except (ValueError, Product.DoesNotExist):
        messages.error(
            request,
            'Checkout could not be completed. '
            'Please check product availability.'
        )
        return redirect('cart_view')


@login_required
def order_success(request, order_id):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    order = get_object_or_404(
        Order,
        pk=order_id,
        buyer=request.user
    )

    return render(
        request,
        'ecommerce/order_success.html',
        {'order': order}
    )


@login_required
@require_POST
def submit_review(request, product_id):
    if request.user.role != 'buyer':
        return redirect('dashboard')

    product = get_object_or_404(Product, pk=product_id)

    rating = request.POST.get('rating')
    comment = request.POST.get('comment', '').strip()

    try:
        rating = int(rating)
    except (TypeError, ValueError):
        messages.error(request, 'Please select a valid rating.')
        return redirect('product_catalogue')

    if rating not in range(1, 6) or not comment:
        messages.error(
            request,
            'Please provide a rating between 1 and 5 and a comment.'
        )
        return redirect('product_catalogue')

    purchased = Order.objects.filter(
        buyer=request.user,
        status='completed',
        items__product=product
    ).exists()

    Review.objects.create(
        buyer=request.user,
        product=product,
        rating=rating,
        comment=comment,
        is_verified=purchased
    )

    if purchased:
        messages.success(request, 'Your verified review was submitted.')
    else:
        messages.success(request, 'Your unverified review was submitted.')

    return redirect('product_catalogue')
