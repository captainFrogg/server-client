import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpErrorResponse
} from '@angular/common/http';
import { Injectable, Injector } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, tap } from 'rxjs';
import { AuthenticationService } from '../services/authentication.service';
import { SnackbarService } from '../services/snackbar.service';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  private httpHeaders = {
    'Content-Type': 'application/json',
    Authorization: ''
  };

  constructor(
    private authenticationService: AuthenticationService,
    private router: Router,
    private readonly injector: Injector
  ) {}

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const authToken = this.authenticationService.getAuthToken();
    request.headers.set('Content-Type', 'application/json');
    if (authToken) {
      this.httpHeaders.Authorization = `Bearer ${authToken}`;
    }
    request = request.clone({
      setHeaders: this.httpHeaders
    });

    return next.handle(request).pipe(
      tap(
        (event: HttpEvent<any>) => {},
        (err: any) => {
          if (err instanceof HttpErrorResponse) {
            if (err.status === 401) {
              const snackbarService = this.injector.get(SnackbarService);

              snackbarService.warning('Vous avez été déconnecté');
              this.authenticationService.logout();
              this.router.navigate(['login']);
            }
          }
        }
      )
    );
  }
}
