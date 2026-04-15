import { HttpClient } from '@angular/common/http';
import { Component, inject, Injectable, signal } from '@angular/core';

@Component({
  selector: 'app-http',
  imports: [],
  templateUrl: './http.html',
  styleUrl: './http.css',
})
export class Http {
  httpClient = inject(HttpClient);
  apiUrl = "https://api.github.com/users/"
  user="afriadenrich";
  usuarioRecibido= signal<any>(null);

  traer(){
    const peticion = this.httpClient.get(this.apiUrl + this.user);

    peticion.subscribe((data) =>{
      if (data) {
        this.usuarioRecibido.set(data);
      }
    })
  }
}
