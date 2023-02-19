import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {map} from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http : HttpClient) { }

  getProduct(){
    return this.http.get<any>("http://192.168.178.70:8383/v1/get_all_bag")
    .pipe(map((res:any)=>{
      return res;
    }))
  }

  checkProduct(bag: any, isChecking: any ) {
    return this.http.post<any>("http://192.168.178.70:8383/v1/checked_bag", {'id': bag.id, 'is_checking': isChecking})
    .pipe(map((res:any)=>{
      return res;
    }))
  }
}
