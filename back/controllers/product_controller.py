from repository.product_repository import ProductRepository   
class ProductController:
    @staticmethod
    async def get_products():
        return ProductRepository.get_products()

    @staticmethod
    async def get_products_duplicate():
        return {"message": "Hello from FastAPI backend Duplicate!"}