import { HttpError } from '../app.reducers'
export interface User {
  username: string;
  password: string;
  email: string;
  phone_no: string;
  email_alert: boolean;
  sms_alert: boolean
}


export interface AuthState {
  authenticated: boolean;
  isActive: boolean;
  errors: HttpError[];
  loading: boolean;
  payload: any;
}

export interface credentials  {
  email: string;
  password: string;
}