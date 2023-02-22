import { Injectable } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TranslationService {
  constructor(private translateService: TranslateService) {}

  public initTranslate() {
    this.translateService.setDefaultLang('fr');
    // the lang to use, if the lang isn't available, it will use the current loader to get them
    this.translateService.use('fr');
  }

  public translate(word: string): Observable<string> {
    return this.translateService.get(word);
  }
}
