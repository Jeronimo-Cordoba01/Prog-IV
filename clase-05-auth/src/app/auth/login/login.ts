import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ILogin } from '../auth.interfaces';

@Component({
  selector: 'app-login-button',
  imports: [ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  formulario = new FormGroup({
    email: new FormControl("", [Validators.email, Validators.required]),
    nombre: new FormControl("", Validators.required),
    password: new FormControl("", Validators.required)
  });
  authService: any;

  accion(){
    this.authService.loguear(this.formulario.value as ILogin);
  }
}
