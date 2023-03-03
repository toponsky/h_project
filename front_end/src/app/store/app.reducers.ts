import { ActionReducerMap } from '@ngrx/store';
import {HttpErrorResponse} from '@angular/common/http';
import * as auth from '../store/auth/auth.reducer';
import { AuthState } from './auth/auth.interface'


export interface HttpError {
  error: HttpErrorResponse;
  errorEffect: string;
}

export interface AppState {
  auth: AuthState;
}

export const reducers: ActionReducerMap<AppState, any> = {
  auth: auth.authReducer
};
