from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms import ProductForm
from ..models import Product
from ..extensions import db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/products")
def list_products():
    products = Product.query.all()
    return render_template("admin/list_products.html", products=products)


@admin_bp.route("/products/new", methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            price=form.price.data,
            stock=form.stock.data,
            description=form.description.data,
        )
        db.session.add(product)
        db.session.commit()
        flash("Produit ajouté avec succès ✅")
        return redirect(url_for("admin.list_products"))
    return render_template("admin/create_product.html", form=form)
