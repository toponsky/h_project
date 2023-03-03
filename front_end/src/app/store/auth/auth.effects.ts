import {Injectable} from '@angular/core';
import {Actions, Effect, ofType} from '@ngrx/effects';
import {Router} from '@angular/router';
import * as AuthActions from './auth.actions';
import {TokenService} from '../../service/token.service';
import { AuthState, credentials } from './auth.interface';
import {of} from 'rxjs';
import {catchError, concatMap, map, switchMap} from 'rxjs/operators';


@Injectable()
export class AuthEffects {


  @Effect()
  signIn = this.actions$
    .pipe(ofType(AuthActions.SIGN_IN),
      map((action: AuthActions.SignIn) => {
        return action.payload
      }),
      switchMap((credentials: credentials) => {
        return this.tokenService.obtainAccessToken(credentials)
          .pipe(switchMap(res => {
            this.tokenService.saveToken(res);
            this.router.navigate(['']);
            return [
              {type: AuthActions.SIGN_IN_SUCCESS},
            ]
          }), catchError(error => {
          return of(
            new AuthActions.AuthError(
              {error: error, errorEffect: AuthActions.SIGN_IN}));
        }))
      }));
  
  @Effect()
  signOut = this.actions$
    .pipe(ofType(AuthActions.SIGN_OUT),
      concatMap((action: AuthActions.SignOut) => {
        this.tokenService.removeToken();
        this.router.navigate(['/login']);
        return [
          {
            type: AuthActions.SIGN_OUT_SUCCESS
          }
        ]
      }));

  @Effect()
  checkIfLoggedIn = this.actions$
    .pipe(ofType(AuthActions.CHECK_IF_LOGGED_IN),
      switchMap((action: AuthActions.CheckIfLoggedIn) => {
        if (this.tokenService.checkIfTokenExists()) {
          return [
            {
              type: AuthActions.SIGN_IN_SUCCESS
            }
          ];
        } else {
          return [{
            type: AuthActions.SIGN_OUT_SUCCESS
          }]
        }
      }));    


  constructor(private actions$: Actions, private tokenService: TokenService,
              private router: Router) {
  }
}
