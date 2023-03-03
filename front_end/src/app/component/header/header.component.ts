import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {Store} from '@ngrx/store';
import {Observable} from 'rxjs';
import { SignOut } from 'src/app/store/auth/auth.actions';
import { TokenService } from '../../service/token.service';
import { AppState } from '../../store/app.reducers';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  authState: Observable<{ authenticated: boolean, isActive: boolean }>;

  constructor(private store: Store<AppState>, private tokenService: TokenService,  private router: Router) { }

  ngOnInit(): void {
    this.authState = this.store.select('auth')
  }

  logout(): void {
    this.store.dispatch(new SignOut());
  }
}
