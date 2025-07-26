import { CommonModule } from "@angular/common";
import { Component, inject } from "@angular/core";
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from "@angular/forms";

@Component({
  selector: "app-contact",
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: "./contact.component.html",
  styleUrl: "./contact.component.css",
})
export class ContactComponent {
  private readonly formBuilder = inject(FormBuilder);
  contactForm: FormGroup;
  successMessage: string | null = null;

  constructor() {
    this.contactForm = this.formBuilder.group({
      email: [""],
      message: [""],
    });
  }

  // Getters for form controls
  get email() {
    return this.contactForm.get("email")!;
  }

  get message() {
    return this.contactForm.get("message")!;
  }

  // Handle form submission
  onSubmit(): void {
    if (this.contactForm.valid) {
      console.log("Formulaire envoyé :", this.contactForm.value);
      this.successMessage = "Demande de contact envoyée avec succès.";
      this.contactForm.reset(); // Reset the form after submission
    }
  }
}
