import { inject } from "@angular/core";
import { ActivatedRouteSnapshot, Routes } from "@angular/router";
import { ProductListComponent } from "./features/product-list/product-list.component";
import { ProductPanelComponent } from "./features/product-panel/product-panel.component";

export const PRODUCTS_ROUTES: Routes = [
  {
    path: "list",
    component: ProductListComponent,
  },
  {
    path: "panel",
    component: ProductPanelComponent,
  },
  { path: "**", redirectTo: "list" },
];
