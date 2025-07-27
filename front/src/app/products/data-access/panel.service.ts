import { Injectable, signal } from "@angular/core";
import { Product } from "./product.model";

@Injectable({
  providedIn: "root",
})
export class PanelService {
  private readonly _cart = signal<Product[]>([]);

  public readonly cart = this._cart.asReadonly();

  // Add a product to the cart
  public addToCart(product: Product): void {
    this._cart.update((cart) => [...cart, product]);
  }

  // Remove a product from the cart
  public removeFromCart(productId: number): void {
    let removed = false;
    this._cart.update((cart) =>
      cart.filter((product) => {
        if (!removed && product.id === productId) {
          removed = true; // Mark the first matching product as removed
          return false; // Exclude this product from the updated cart
        }
        return true;
      })
    );
    console.log("Produit retiré du panier :", productId);
  }

  // Clear the cart
  public clearCart(): void {
    this._cart.set([]);
    console.log("Panier vidé.");
  }

  // Get the current cart items
  public getCartItems(): Product[] {
    return this._cart();
  }
}
