import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api.service';
import { __read } from 'tslib';
import * as fromApp from '../../store/app.reducers';
import * as AuthActions from "../../store/auth/auth.actions";
import {Store} from '@ngrx/store';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {

  public productList : any ;
  public filterList : any;
  public filterCondition: any;
  public filterValue: any;
  public amount : any;
  searchKey:string ="";
  constructor(private store: Store<fromApp.AppState>, private api : ApiService) { }

  ngOnInit(): void {
    this.store.dispatch(new AuthActions.CheckIfLoggedIn());
    this.api.getProduct()
    .subscribe(res=>{
      this.productList = res;
      this.filterList = res;
      this.amount = res.length;
      this.filterCondition = 'all'
    });
  }
  
  checkingBag(item: any){
    this.api.checkProduct(item, true)
    .subscribe(res=>{
      item.is_checking = true
      this._freshList()
    });
  }

  uncheckingBag(item: any){
    this.api.checkProduct(item, false)
    .subscribe(res=>{
      item.is_checking = false
      this._freshList()
    });
  }

  filter(filterCondition: string){
    this.filterCondition =filterCondition
    console.log(filterCondition)
    let prop = '', value = true;
    if(this.filterCondition == "checked") {
      this.filterValue = true;
    } else if (this.filterCondition == 'non-checked') {
      this.filterValue = false;
    } 
   this._freshList()
  }

  _freshList() {
    this.filterList = this.productList
    .filter((a:any)=>{
      if(a['is_checking'] == this.filterValue || this.filterCondition == 'all'){
        return a;
      }
    })
    this.amount = this.filterList.length
  }

  getCheckedBackground(bag: any) {
    return bag.is_checking? "green": '';
  }
    

}
