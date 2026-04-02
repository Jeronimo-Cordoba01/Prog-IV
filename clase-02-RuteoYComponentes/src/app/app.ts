import { Component, signal } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
//import { Dashboard } from "./page/dashboard/dashboard";

/**
 *El componente APP formado por app.html, app.css y app.ts
  App es una excepción. Es un componente Global. Todo renderiza dentro de app
 */
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('clase-02-RuteoYComponentes');
}
