import { CommonModule } from "@angular/common";
import { Component, inject } from "@angular/core";
import { PanelService } from "app/products/data-access/panel.service";
import { Product } from "app/products/data-access/product.model";

@Component({
  selector: "app-product-panel",
  standalone: true,
  imports: [CommonModule],
  templateUrl: "./product-panel.component.html",
  styleUrl: "./product-panel.component.css",
})
export class ProductPanelComponent {
  private readonly panelService = inject(PanelService);

  cartItems: Product[] = [];

  ngOnInit(): void {
    this.cartItems = this.panelService.getCartItems();
  }
}
