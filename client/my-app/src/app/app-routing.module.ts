import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () =>
      import('./modules/home/home.module').then((m) => m.HomeModule),
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./standalone-components/login/login.component').then(
        (mod) => mod.LoginComponent
      ),
  },
  {
    path: 'sign-up',
    loadComponent: () =>
      import('./standalone-components/sign-up/sign-up.component').then(
        (mod) => mod.SignUpComponent
      ),
  },
  {
    path: '**',
    redirectTo: 'home',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
