import { Component, effect, inject } from "@angular/core";
import { Router, RouterModule } from "@angular/router";
import { SplitterModule } from "primeng/splitter";
import { ToolbarModule } from "primeng/toolbar";
import { PanelMenuComponent } from "./shared/ui/panel-menu/panel-menu.component";
import { PanelService } from "./products/data-access/panel.service";
import { CommonModule } from "@angular/common";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
  standalone: true,
  imports: [
    RouterModule,
    SplitterModule,
    ToolbarModule,
    PanelMenuComponent,
    CommonModule,
  ],
})
export class AppComponent {
  private readonly panelService = inject(PanelService);
  private readonly router = inject(Router);

  title = "ALTEN SHOP";
  cartItemCount = 0;

  constructor() {
    effect(() => {
      this.cartItemCount = this.panelService.cart().length;
    });
  }

  public goToPanelProducts(): void {
    this.router.navigate(["/products/panel"]);
  }
}
