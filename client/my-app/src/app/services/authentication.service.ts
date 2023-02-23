import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { mergeMap, catchError, map } from 'rxjs/operators';
import { ConfigurationService } from './configuration.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  public authUser: any;

  public authToken: string | null = null;

  constructor(
    private configurationService: ConfigurationService,
    private httpClient: HttpClient
  ) {}

  public signUp(
    email: string,
    username: string,
    password: string
  ): Observable<any> {
    return this.httpClient.post(
      `${this.configurationService.serverUrl}/sign-up`,
      {
        email,
        username,
        password
      }
    );
  }

  public login(username: string, password: string): Observable<any> {
    this.cleanToken();
    return this.httpClient
      .post(`${this.configurationService.serverUrl}/login`, {
        username,
        password
      })
      .pipe(
        catchError(error => {
          return throwError(() => error);
        }),
        map((response: any) => {
          this.authToken = response.access_token;
          this.authUser = {
            username: response.username,
            firstName: response.firstName,
            lastName: response.lastName,
            email: response.email
          };
          localStorage.setItem('authToken', response.access_token);
          localStorage.setItem('authUser', JSON.stringify(this.authUser));
          return 'Authentication Success';
        })
      );
  }

  public logout() {
    this.cleanAuthUser();
    this.cleanToken();
  }

  public cleanToken(): void {
    this.authToken = null;
    localStorage.removeItem('authToken');
  }

  public cleanAuthUser(): void {
    this.authUser = null;
    localStorage.removeItem('authUser');
  }

  public getAuthToken(): string | null {
    return this.authToken ? this.authToken : localStorage.getItem('authToken');
  }

  public getAuthUser(): any {
    return this.authUser
      ? this.authUser
      : JSON.parse(
          localStorage.getItem('authUser')
            ? (localStorage.getItem('authUser') as string)
            : ''
        );
  }
}
