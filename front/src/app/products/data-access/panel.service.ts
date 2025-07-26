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
    console.log("Produit ajouté au panier :", product);
  }

  // Remove a product from the cart
  public removeFromCart(productId: number): void {
    this._cart.update((cart) =>
      cart.filter((product) => product.id !== productId)
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
