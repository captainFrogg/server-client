import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ConfigurationService } from './configuration.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(
    private configurationService: ConfigurationService,
    private httpClient: HttpClient
  ) {}

  public getUser(id: number): Observable<any> {
    return this.httpClient.get(`${this.configurationService.serverUrl}/user`, {
      params: {
        id
      }
    });
  }

  public listUsers(): Observable<any> {
    return this.httpClient.get(
      `${this.configurationService.serverUrl}/user`,
      {}
    );
  }
}
