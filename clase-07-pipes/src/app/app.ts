import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CurrencyPipe, DatePipe, TitleCasePipe, UpperCasePipe } from '@angular/common';
import { JsonPipe } from '@angular/common';
import { AcortadorPipe } from './pipes/acortador-pipe';
import { SegundosPipe } from './pipes/segundos-pipe';
import { FechaPipe } from './pipes/fecha-pipe-pipe';

@Component({
  selector: 'app-root',
  imports: [TitleCasePipe, JsonPipe, DatePipe, UpperCasePipe, CurrencyPipe, AcortadorPipe, SegundosPipe, FechaPipe],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  dni = 12345678;
  nombre0 = 'Juan';
  nombre1 = 'Juan';
  nombre2 = 'Juan';
  nombre3 = 'Juan';

  objeto = { clave: 'valor', clave2: 'valor2' };
  //stringify = (obj: Object) => JSON.stringify(obj);

  fechaEnString = "2026-12-31";
  fechaLarga = "2026-12-31T23:59:59";
  fechaNumero = 1704067199000;
  fechaDate = new Date('2026-12-31T00:00:00');

  textoCorto = "Hola";
  textoLargo = "Este es un texto muy largo que quiero acortar";
}
