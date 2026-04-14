import { Component, input, InputSignal, output } from '@angular/core';
import { RouterLink } from "@angular/router";

@Component({
  selector: 'app-card',
  imports: [RouterLink],
  templateUrl: './card.html',
  styleUrl: './card.css',
})
export class Card {
  //imagen: string = "clase-03-input-output\public\img\nanite 1.jpg";
  //titulo: string = "titulo";
  //subtitulo: string = "subtitulo";
  //link: string = "link";
  //textoLink: string = "textoLink";
  // value: number = 0;
  value= input(0);

  imagen: InputSignal<string> = input("clase-03-input-output\public\img\nanite 1.jpg");
  titulo: InputSignal<string> = input("titulo");
  subtitulo: InputSignal<string> = input("subtitulo");
  link: InputSignal<string> = input("link");
  textoLink: InputSignal<string> = input("textoLink");

  avisoQueSeClickeoLaCard= output<string>(); //La función que avisa

  cardClickeada(){
    const titulo = this.titulo();
    console.log(titulo);
    this.avisoQueSeClickeoLaCard.emit(titulo);
  }
}
