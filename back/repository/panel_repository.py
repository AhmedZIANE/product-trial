# repository/cart_repository.py
from models.panel_model import Cart, CartItem
from sqlalchemy.future import select

class PanelRepository:

    @staticmethod
    async def get_or_create_cart(session, user_id):
        result = await session.execute(select(Cart).where(Cart.user_id == user_id))
        cart = result.scalars().first()
        if not cart:
            cart = Cart(user_id=user_id)
            session.add(cart)
            await session.commit()
            await session.refresh(cart)
        return cart

    @staticmethod
    async def add_item_to_cart(session, cart_id, product_id, quantity):
        result = await session.execute(
            select(CartItem).where(CartItem.cart_id == cart_id, CartItem.product_id == product_id)
        )
        item = result.scalars().first()
        if item:
            item.quantity += quantity
        else:
            item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
            session.add(item)
        await session.commit()

    @staticmethod
    async def remove_item_from_cart(session, cart_id, product_id):
        await session.execute(
            CartItem.__table__.delete().where(CartItem.cart_id == cart_id, CartItem.product_id == product_id)
        )
        await session.commit()

    @staticmethod
    async def clear_cart(session, cart_id):
        await session.execute(CartItem.__table__.delete().where(CartItem.cart_id == cart_id))
        await session.commit()

    @staticmethod
    async def get_cart_items(session, cart_id):
        result = await session.execute(select(CartItem).where(CartItem.cart_id == cart_id))
        return result.scalars().all()
