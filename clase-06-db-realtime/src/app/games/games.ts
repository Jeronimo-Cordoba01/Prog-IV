import { Component, inject } from '@angular/core';
import { Supabase } from '../services/supabase';

@Component({
  selector: 'app-games',
  imports: [],
  templateUrl: './games.html',
  styleUrl: './games.css',
})
export class Games {
  supabaseService = inject(Supabase);

  traer() {
    this.supabaseService.traer();
  }

  insertar() {
    this.supabaseService.insertar();
  }
  modificar() {
    this.supabaseService.modificar();
  }
  eliminar() {
    this.supabaseService.eliminar();
  }
}