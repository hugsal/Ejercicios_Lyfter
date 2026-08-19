from entities.cartEntity import Cart, CartItem
from entities.productEntity import Product
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload


class CartRepository:
    @staticmethod
    def format_cart(cart):
        if not cart:
            return None
        formatted_items = []
        total_amount = 0.0
        for item in cart.items:
            product = item.product
            product_data = (
                {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                }
                if product
                else None
            )
            item_price = product.price if product else 0.0
            subtotal = item_price * item.quantity
            total_amount += subtotal

            formatted_items.append(
                {
                    "id": item.id,
                    "productId": item.fk_product_id,
                    "product": product_data,
                    "quantity": item.quantity,
                    "unitPrice": item_price,
                    "subtotal": subtotal,
                }
            )

        return {
            "id": cart.id,
            "userId": cart.fk_user_id,
            "status": cart.status,
            "createdAt": cart.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if cart.created_at
            else None,
            "updatedAt": cart.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            if cart.updated_at
            else None,
            "items": formatted_items,
            "totalAmount": total_amount,
        }

    @staticmethod
    def get_or_create_active_cart(db, user_id):
        stmt = (
            select(Cart)
            .options(selectinload(Cart.items).joinedload(CartItem.product))
            .where(Cart.fk_user_id == user_id, Cart.status == "active")
            .order_by(Cart.created_at.desc())
        )
        cart = db.scalar(stmt)
        if not cart:
            cart = Cart(fk_user_id=user_id, status="active")
            db.add(cart)
            db.commit()
            return CartRepository.get_cart_by_id(db, cart.id)
        return CartRepository.format_cart(cart)

    @staticmethod
    def get_cart_entity_by_id(db, cart_id):
        stmt = (
            select(Cart)
            .options(selectinload(Cart.items).joinedload(CartItem.product))
            .where(Cart.id == int(cart_id))
        )
        return db.scalar(stmt)

    @staticmethod
    def get_cart_by_id(db, cart_id):
        stmt = (
            select(Cart)
            .options(selectinload(Cart.items).joinedload(CartItem.product))
            .where(Cart.id == int(cart_id))
        )
        cart = db.scalar(stmt)
        if not cart:
            return None
        return CartRepository.format_cart(cart)

    @staticmethod
    def get_user_carts(db, user_id):
        stmt = (
            select(Cart)
            .options(selectinload(Cart.items).joinedload(CartItem.product))
            .where(Cart.fk_user_id == user_id)
            .order_by(Cart.created_at.desc())
        )
        carts = db.scalars(stmt).unique().all()
        return list(map(CartRepository.format_cart, carts))

    @staticmethod
    def add_or_update_item(db, cart_id, product_id, quantity):
        cart = db.get(Cart, int(cart_id))
        if not cart:
            return None

        stmt = select(CartItem).where(
            CartItem.fk_cart_id == cart_id, CartItem.fk_product_id == product_id
        )
        item = db.scalar(stmt)

        if quantity <= 0:
            if item:
                db.delete(item)
                db.commit()
        else:
            if item:
                item.quantity = quantity
            else:
                item = CartItem(
                    fk_cart_id=cart_id, fk_product_id=product_id, quantity=quantity
                )
                db.add(item)
            db.commit()

        return CartRepository.get_cart_by_id(db, cart_id)

    @staticmethod
    def remove_item(db, cart_id, product_id):
        stmt = select(CartItem).where(
            CartItem.fk_cart_id == cart_id, CartItem.fk_product_id == product_id
        )
        item = db.scalar(stmt)
        if item:
            db.delete(item)
            db.commit()
        return CartRepository.get_cart_by_id(db, cart_id)

    @staticmethod
    def update_cart_status(db, cart_id, status):
        cart = db.get(Cart, int(cart_id))
        if cart:
            cart.status = status
            db.commit()
            return CartRepository.get_cart_by_id(db, cart_id)
        return None

