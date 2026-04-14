import { Component } from '@angular/core';
import { Card } from '../../components/card/card';

@Component({
  selector: 'app-tutoriales',
  imports: [Card],
  templateUrl: './tutoriales.html',
  styleUrl: './tutoriales.css',
})
export class Tutoriales {
  cards: Array<any> = [
  {
  tituloOriginal:"Aprende Angular en tu navegador",
  subtituloOriginal:"a traves del patio de juegos",
  imagenOriginal:"clase-03-input-output\public\img\nanite-1.jpg",
  textoLinkOriginal:"Comienza a programar",
  linkOriginal:"",
  },
  {
  tituloOriginal:"Señales de aprendizaje2",
  subtituloOriginal:"a traves del patio de juegos",
  imagenOriginal:"clase-03-input-output\public\img\nanite-1.jpg",
  textoLinkOriginal:"Comienza a programar",
  linkOriginal:"",
  },
];

ultimaCard='';
  meAvisaronQueClickearonUnaCard(titulo: string){
    this.ultimaCard = titulo;
  }

}

// Esto debería estar en otro archivo app/interface/Icard.ts o app/components/card/Icard.ts, etc.
interface ICard{
  tituloOriginal: string;
  subtituloOriginal: string;
  imagenOriginal: string;
  textoLinkOriginal: string;
  linkOriginal: string;
}
