import { Routes } from '@angular/router';
import { Chat } from './chat/chat';
import { Games } from './games/games';

export const routes: Routes = [
  {
    path: 'chat',
    component: Chat,
  },
  {
    path: 'games',
    component: Games,
  },
];