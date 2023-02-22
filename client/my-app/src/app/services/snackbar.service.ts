import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { TranslationService } from './translate.service';

@Injectable({
  providedIn: 'root'
})
export class SnackbarService {
  constructor(
    private snackbar: MatSnackBar,
    private translationService: TranslationService
  ) {}

  public async success(msg: string) {
    this.snackbar.open(
      msg,
      await this.translationService.translate('CLOSE').toPromise(),
      {
        horizontalPosition: 'center',
        verticalPosition: 'top',
        duration: 3000,
        panelClass: ['mat-toolbar', 'mat-primary']
      }
    );
  }

  public async warning(msg: string) {
    this.snackbar.open(
      msg,
      await this.translationService.translate('CLOSE').toPromise(),
      {
        horizontalPosition: 'center',
        verticalPosition: 'top',
        duration: 3000,
        panelClass: ['mat-toolbar', 'mat-accent']
      }
    );
  }

  public async error(msg: string) {
    this.snackbar.open(
      msg,
      await this.translationService.translate('CLOSE').toPromise(),
      {
        horizontalPosition: 'center',
        verticalPosition: 'top',
        duration: 3000,
        panelClass: ['mat-toolbar', 'mat-warn']
      }
    );
  }
}
