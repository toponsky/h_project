import { Injectable } from '@angular/core';
import {MatSnackBar, MatSnackBarConfig } from '@angular/material/snack-bar';
@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  config: MatSnackBarConfig = {
    duration: 4000
  };

  constructor(public snackBar: MatSnackBar) {

  }

  showSuccessMsg(msg: any) {
    this.config['panelClass'] = ['notification', 'success'];
    this.snackBar.open(msg, '', this.config);
  }

  showWarnMsg(msg: any) {
    this.config['panelClass'] = ['notification', 'success'];
    this.snackBar.open(msg, '', this.config);
  }

  showFailMsg(msg: any) {
    this.config['panelClass'] = ['notification', 'fail'];
    this.snackBar.open(msg, '', this.config);
  }
}
