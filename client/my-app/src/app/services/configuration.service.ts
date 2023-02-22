import { Injectable } from '@angular/core';
import { environment } from '../../environment/environment';

@Injectable({
  providedIn: 'root',
})
export class ConfigurationService {
  public serverUrl = environment.serverUrl;

  constructor() {}
}
