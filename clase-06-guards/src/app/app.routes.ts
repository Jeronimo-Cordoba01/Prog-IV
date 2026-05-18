import { Routes } from '@angular/router';
import { authRoutes } from './auth/auth.route';
import { Ahorcado } from './games/ahorcado/ahorcado';
import { Resultados } from './resultados/resultados';
import { estaLogueadoGuard } from './guards/esta-logueado-guard';
export const routes: Routes = [
    {
        path: 'auth',
        children: authRoutes,
    },
    {
        path: 'ahorcado',
        loadComponent: () => import('./games/ahorcado/ahorcado').then((c) => c.Ahorcado), canActivate: [estaLogueadoGuard],
    },
    {
        path: 'resultados',
        component: Resultados,
    },
];