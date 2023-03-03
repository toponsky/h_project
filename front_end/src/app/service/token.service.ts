import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {credentials} from '../store/auth/auth.interface';
import { environment } from 'src/environments/environment';


@Injectable()
export class TokenService {


  baseUrl = environment.baseUrl + environment.api_version;

  constructor(private httpClient: HttpClient) {
  }

  obtainAccessToken(auth: credentials) {
    return this.httpClient.post<string>(this.baseUrl + '/token', {
      email: auth.email,
      password: auth.password
    }, {
      headers: {'Content-type': 'application/json; charset=utf-8'}
    });
  }

  saveToken(token: String): void {
    localStorage.setItem('admin_usr', JSON.stringify(token));
  }


  removeToken() {
    localStorage.removeItem('admin_usr');
  }

  getToken() {
    const storageToken = localStorage.getItem('admin_usr');
    let token = '';
    if (storageToken != null || storageToken != undefined) {
      token = JSON.parse(storageToken).access_token;
    }
    return token;
  }

  getRefreshToken() {
    const storageRefreshToken = localStorage.getItem('admin_usr');
    let refreshToken = '';
    if (storageRefreshToken != null || storageRefreshToken != undefined) {
      refreshToken = JSON.parse(storageRefreshToken).refresh_token;
    }
    return refreshToken;
  }

  checkIfTokenExists() {
    return localStorage.getItem('admin_usr') != null || localStorage.getItem('admin_usr') != undefined;
  }
}
