import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {map} from 'rxjs/operators';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseUrl = environment.baseUrl + environment.api_version + environment.api_secured;
  constructor(private http : HttpClient) { }
  
  getProduct(){
    return this.http.get<any>(this.baseUrl + "/get_all_bag")
    .pipe(map((res:any)=>{
      return res;
    }))
  }

  checkProduct(bag: any, isChecking: any ) {
    return this.http.post<any>(this.baseUrl + "/checked_bag", {'id': bag.id, 'is_checking': isChecking})
    .pipe(map((res:any)=>{
      return res;
    }))
  }
}
