import {Injectable} from '@angular/core';
import {HttpHandler, HttpInterceptor, HttpRequest} from '@angular/common/http';
import {BehaviorSubject, of, throwError} from 'rxjs';
import {Router} from '@angular/router';
import {catchError} from 'rxjs/operators';
import { environment } from 'src/environments/environment';

import { TokenService } from '../../service/token.service';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {

  isRefreshingToken:boolean = false;
  tokenSubject: BehaviorSubject<string> = new BehaviorSubject<string>('');

  constructor(private tokenService: TokenService, private router: Router) {
  }

  addTokenToHeader(request: HttpRequest<any>, token: any): HttpRequest<any> {
    if (token != null) {
      return request.clone({
        setHeaders: {
          Authorization: 'Bearer ' + token.access_token
        }
      });
    }
    return request.clone({
      setHeaders: {
        Authorization: 'Bearer ' + this.tokenService.getToken()
      }
    });
  }

  intercept(request: HttpRequest<any>, next: HttpHandler): any {
    if (request.url.includes(environment.api_secured)) {
      if (!this.tokenService.getToken()) {
        this.router.navigate(['/login']);
      } else {
        return next.handle(this.addTokenToHeader(request, null)).pipe(catchError(
          error => {
            this.router.navigate(['/login']);
            return throwError(error);
          }
        ));
      }
    } else {
      return next.handle(request);
    }
  }

}
