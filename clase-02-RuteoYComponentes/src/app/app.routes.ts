import { Routes } from '@angular/router';
import { Login } from './page/login/login';
import { Home } from './page/home/home';
import { Dashboard } from './page/dashboard/dashboard';
import { Error } from './page/error/error';

/**
* El archivo app.routes.ts es el encargado de definir las rutas de la aplicación.
* Asocian nombres a componentes. Es decir, cada ruta tiene un componente asociado que se renderiza cuando se accede a esa ruta.
* Permite varias configuraciones
 */

export const routes: Routes = [
    {path: "home", component: Home},
    //Cuando se entre a /home, borrar lo que haya en el router outlet, e instanciar HOME
    {path: '', redirectTo: 'home', pathMatch: 'prefix'},
    //{path: "", component: Home}, //Ruta vacía
    //Cuando se entre a /home, borrar lo que haya en el router outlet, e instanciar HOME
    {path: "login", component: Login},
    {path: "dashboard", component: Dashboard},
    {path: "**", component: Error}, //Comodín -> Cualquier ruta que no esté definida
];
