import { Routes } from '@angular/router';
import { authRoutes } from './auth/auth.route';

export const routes: Routes = [
    {
        path:'auth',
        children: authRoutes,
    },
];
