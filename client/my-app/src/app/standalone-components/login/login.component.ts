import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { TranslationService } from 'src/app/services/translate.service';
import { SnackbarService } from 'src/app/services/snackbar.service';
import { Router } from '@angular/router';
import { lastValueFrom } from 'rxjs';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatCardModule,
    TranslateModule,
  ],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  public form!: FormGroup;

  constructor(
    private authenticationService: AuthenticationService,
    private translationService: TranslationService,
    private snackbarService: SnackbarService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.form = new FormGroup({
      username: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    });
  }

  selectSignup(): void {
    this.router.navigateByUrl('/sign-up');
  }

  submit(): void {
    this.authenticationService
      .login(this.form.value.username, this.form.value.password)
      .subscribe({
        next: async () => {
          this.snackbarService.success(
            await lastValueFrom(
              this.translationService.translate('AUTHENTICATION_SUCCESS')
            )
          );

          this.router.navigate(['home']);
        },
        error: async (error) => {
          this.snackbarService.error(
            await lastValueFrom(
              this.translationService.translate('AUTHENTICATION_ERROR')
            )
          );
        },
      });
  }
}
