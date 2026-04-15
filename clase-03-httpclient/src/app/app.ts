import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Http } from './services/http/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  http = inject(Http);
  
  ngOnInit(){
    this.http.traer()
  }
}
