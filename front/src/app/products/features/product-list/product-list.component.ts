import { CommonModule, CurrencyPipe } from "@angular/common";
import { Component, OnInit, inject, signal } from "@angular/core";
import { PanelService } from "app/products/data-access/panel.service";
import { Product } from "app/products/data-access/product.model";
import { ProductsService } from "app/products/data-access/products.service";
import { ProductFormComponent } from "app/products/ui/product-form/product-form.component";
import { ButtonModule } from "primeng/button";
import { CardModule } from "primeng/card";
import { DataViewModule } from "primeng/dataview";
import { DialogModule } from "primeng/dialog";
import { PaginatorModule } from "primeng/paginator";

const emptyProduct: Product = {
  id: 0,
  code: "",
  name: "",
  description: "",
  image: "",
  category: "",
  price: 0,
  quantity: 0,
  internalReference: "",
  shellId: 0,
  inventoryStatus: "INSTOCK",
  rating: 0,
  createdAt: 0,
  updatedAt: 0,
};

@Component({
  selector: "app-product-list",
  templateUrl: "./product-list.component.html",
  styleUrls: ["./product-list.component.scss"],
  standalone: true,
  imports: [
    DataViewModule,
    CardModule,
    ButtonModule,
    DialogModule,
    ProductFormComponent,
    CurrencyPipe,
    CommonModule,
    PaginatorModule,
  ],
})
export class ProductListComponent implements OnInit {
  private readonly productsService = inject(ProductsService);
  private readonly panelService = inject(PanelService);

  public readonly products = this.productsService.products;

  public isDialogVisible = false;
  public isCreation = false;
  public readonly editedProduct = signal<Product>(emptyProduct);

  paginatedProducts: Product[] = []; // Products for the current page
  rowsPerPage = 5; // Number of products per page
  currentPage = 0; // Current page index

  ngOnInit() {
    this.productsService.get().subscribe(() => {
      this.updatePaginatedProducts(); // Update paginated products after fetching
    });
  }

  public onCreate() {
    this.isCreation = true;
    this.isDialogVisible = true;
    this.editedProduct.set(emptyProduct);
  }

  public onUpdate(product: Product) {
    this.isCreation = false;
    this.isDialogVisible = true;
    this.editedProduct.set(product);
  }

  public onDelete(product: Product) {
    this.productsService.delete(product.id).subscribe();
  }

  public onAddToCart(product: Product): void {
    this.panelService.addToCart(product);
    console.log("Produit ajouté au panier :", product);
  }

  public isInCart(product: Product): boolean {
    return this.panelService
      .getCartItems()
      .some((cartItem) => cartItem.id === product.id);
  }

  public onRemoveFromCart(product: Product): void {
    this.panelService.removeFromCart(product.id);
  }

  public onPageChange(event: any): void {
    this.currentPage = event.page;
    this.updatePaginatedProducts();
  }

  public onSave(product: Product) {
    if (this.isCreation) {
      this.productsService.create(product).subscribe();
    } else {
      this.productsService.update(product).subscribe();
    }
    this.closeDialog();
  }

  public onCancel() {
    this.closeDialog();
  }

  private updatePaginatedProducts(): void {
    const start = this.currentPage * this.rowsPerPage;
    const end = start + this.rowsPerPage;
    this.paginatedProducts = this.products().slice(start, end);
  }

  private closeDialog() {
    this.isDialogVisible = false;
  }
}
