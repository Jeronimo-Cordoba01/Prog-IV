import { Routes } from '@angular/router';
import { Bienvenida } from './bienvenida/bienvenida';
import { Login } from './login/login';
//import { Register } from './register/register';

export const routes: Routes = [
    {path:"", loadComponent:() => import("./bienvenida/bienvenida").then((m)=>m.Bienvenida)},
    {path:"login",loadComponent:() => import("./login/login").then((a)=>a.Login)},
    {path:"register",loadComponent:() => import("./register/register")},// Funciona porque register tiene export DEFAULT
];
