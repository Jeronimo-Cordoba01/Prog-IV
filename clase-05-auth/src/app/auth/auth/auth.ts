import { JsonPipe } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLinkWithHref, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-auth',
  imports: [RouterOutlet, RouterLinkWithHref, JsonPipe,],
  templateUrl: './auth.html',
  styleUrl: './auth.css',
})
export class Auth {
authS: any;
  
}
