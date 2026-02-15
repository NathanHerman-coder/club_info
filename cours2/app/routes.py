from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from .models import Product
from .extensions import db
from .forms import CheckoutForm

main = Blueprint("main", __name__)


@main.route("/")
def index():
    products = Product.query.filter_by(is_active=True).all()
    return render_template("index.html", products=products)


@main.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product)


@main.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get("cart", {})
    qty = int(request.form.get("quantity", 1))
    if str(product_id) in cart:
        cart[str(product_id)] += qty
    else:
        cart[str(product_id)] = qty
    session["cart"] = cart
    flash(f"Ajouté {qty} x {product.name} au panier")
    return redirect(url_for("main.view_cart"))


@main.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.query.get(int(pid))
        if not p:
            continue
        subtotal = float(p.price) * qty
        total += subtotal
        items.append({"product": p, "quantity": qty, "subtotal": subtotal})
    return render_template("cart.html", items=items, total=total)


@main.route("/cart/clear", methods=["POST"])
def clear_cart():
    session.pop("cart", None)
    flash("Panier vidé")
    return redirect(url_for("main.index"))


@main.route("/checkout", methods=["GET", "POST"])
def checkout():
    form = CheckoutForm()
    cart = session.get("cart", {})
    if not cart:
        flash("Votre panier est vide")
        return redirect(url_for("main.index"))

    if form.validate_on_submit():
        # For this minimal implementation we won't persist orders.
        session.pop("cart", None)
        flash("Merci pour votre commande — simulation terminée !")
        return redirect(url_for("main.index"))

    return render_template("checkout.html", form=form)
