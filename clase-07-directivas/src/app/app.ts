import { Component } from '@angular/core';
import { Resaltar } from './directives/resaltar';
import { Timer } from './directives/timer';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  standalone: true,
  imports: [Resaltar, Timer],
  styleUrls: ['./app.css'],
})
export class App {
  algo = 'Hola';

  color = '#f00';

  ngOnInit() {
    setTimeout(() => {
      this.color = '#000';
    }, 3000);
  }
}