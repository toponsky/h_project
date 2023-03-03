import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './service/guard/auth.guard';
import { LoginComponent } from './component/auth/login/login.component';
import { ProductsComponent } from './component/products/products.component';

const routes: Routes = [
  {component: LoginComponent,path:'login'},
  {component:ProductsComponent,
    path:'',
  canActivate: [AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
