import { Component } from '@angular/core';
import { FormArray, FormControl, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  arrayDeControles=[
    new FormControl("",{
      validators: [Validators.minLength(3), Validators.maxLength(15), Validators.required]
    }),
    new FormControl("",{
      validators: [Validators.required]
    }),
    new FormControl("",{
      validators: [Validators.required]
    }),
    new FormControl("",{
      validators: [Validators.required]
    }),
  ];

  formulario = new FormArray(this.arrayDeControles);

  arrayParaLaVista: any[] = [];

  ngOnInit(){
    this.arrayParaLaVista.push({
      type: "text",
      name: "nombre",
      control: this.arrayDeControles[0],
    });
    this.arrayParaLaVista.push({
      type: "text",
      name: "password",
      control: this.arrayDeControles[1],
    });
  }

  /*
  formulario = new FormArray([
    new FormControl("nombre",{
      validators: [Validators.minLength(3), Validators.maxLength(15), Validators.required]
    }),
    new FormControl("apellido",{
      validators: [Validators.required]
    }),
    new FormControl("email",{
      validators: [Validators.required]
    }),
    new FormControl("password",{
      validators: [Validators.required]
    }),
  ]); */
  mostrar(){

  }
}
