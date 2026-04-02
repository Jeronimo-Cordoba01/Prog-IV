import { Component } from '@angular/core';
import { Card } from "../../components/card/card";

@Component({
  selector: 'app-home',
  imports: [Card],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {
  valor = 55;
  ngOnInit(){
    console.log("Se ejecuta ON INIT - antes del render - del después del constructor");
  }

  ngOnDestroy(){
    console.log("Se destruye HOME");
  }
}
