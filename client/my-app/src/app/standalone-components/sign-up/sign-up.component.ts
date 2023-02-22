import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { TranslateModule } from '@ngx-translate/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { SnackbarService } from 'src/app/services/snackbar.service';
import { TranslationService } from 'src/app/services/translate.service';
import { lastValueFrom } from 'rxjs';

@Component({
  selector: 'app-sign-up',
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
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss'],
})
export class SignUpComponent implements OnInit {
  public form!: FormGroup;

  constructor(
    private authenticationService: AuthenticationService,
    private translationService: TranslationService,
    private snackbarService: SnackbarService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.form = new FormGroup({
      email: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$'),
      ]),
      username: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    });
  }

  goToLogin(): void {
    this.router.navigateByUrl('/login');
  }

  submit(): void {
    this.authenticationService
      .signUp(
        this.form.value.email,
        this.form.value.username,
        this.form.value.password
      )
      .subscribe({
        next: async () => {
          this.snackbarService.success(
            await lastValueFrom(
              this.translationService.translate('ACCOUNT_CREATION_SUCCESS')
            )
          );
          this.goToLogin();
        },
        error: async (error) => {
          this.snackbarService.error(
            await lastValueFrom(
              this.translationService.translate('ACCOUNT_CREATION_ERROR')
            )
          );
        },
      });
  }
}
