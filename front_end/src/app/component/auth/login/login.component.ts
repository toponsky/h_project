import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {Store} from '@ngrx/store';
import {Observable} from 'rxjs';
import { HttpError } from '../../../store/app.reducers'
import * as fromApp from '../../../store/app.reducers';
import { SignIn } from '../../../store/auth/auth.actions';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  signInForm: FormGroup;
  emailPattern = '^[a-zA-Z0-9_!#$%&’*+/=?`{|}~^.-]+@[a-zA-Z0-9.-]+$';

  loading: Observable<boolean>;
  error: Observable<HttpError[]>;

  constructor(private store: Store<fromApp.AppState>) {}

  ngOnInit() {
    this.signInForm = new FormGroup({
      'email': new FormControl(null, [Validators.required, Validators.pattern(this.emailPattern)]),
      'password': new FormControl(null, Validators.required),
    });

    this.loading = this.store.select(store => store.auth.loading);
    this.error = this.store.select(store => store.auth.errors);
  }

  onSubmit() {
    this.store.dispatch(new SignIn({
      email: this.signInForm.value.email,
      password: this.signInForm.value.password
    }));
  }

}
