import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginGuard } from './guards/login.guard';
import { LogoutGuard } from './guards/logout.guard';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () =>
      import('./modules/home/home.module').then(m => m.HomeModule),
    canActivate: [LoginGuard]
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./standalone-components/login/login.component').then(
        mod => mod.LoginComponent
      ),
    canActivate: [LogoutGuard]
  },
  {
    path: 'sign-up',
    loadComponent: () =>
      import('./standalone-components/sign-up/sign-up.component').then(
        mod => mod.SignUpComponent
      ),
    canActivate: [LogoutGuard]
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
