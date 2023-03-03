import {Action} from '@ngrx/store';
import {HttpError} from "../app.reducers";
import { credentials } from './auth.interface';
export const SIGN_IN = 'SIGN_IN';
export const SIGN_IN_SUCCESS = 'SIGN_IN_SUCCESS';
export const SIGN_OUT = 'SIGN_OUT';
export const SIGN_OUT_SUCCESS = 'SIGN_OUT_SUCCESS';
export const AUTH_ERROR = 'AUTH_ERROR';
export const CHECK_IF_LOGGED_IN = 'CHECK_IF_LOGGED_IN';




export class SignIn implements Action {
  readonly type = SIGN_IN;

  constructor(public payload: credentials) {
  }
}

export class SignInSuccess implements Action {
  readonly type = SIGN_IN_SUCCESS;
}

export class SignOut implements Action {
  readonly type = SIGN_OUT;
}

export class SignOutSuccess implements Action {
  readonly type = SIGN_OUT_SUCCESS;
}


export class AuthError implements Action {
  readonly type = AUTH_ERROR;

  constructor(public payload: HttpError) {
  }
}

export class CheckIfLoggedIn implements Action {
  readonly type = CHECK_IF_LOGGED_IN;
}

export type AuthActions = SignIn | SignInSuccess
  | SignOut | SignOutSuccess | AuthError | CheckIfLoggedIn