import * as AuthActions from './auth.actions';
import { AuthState } from './auth.interface';

const initialState: AuthState = {
  authenticated: false,
  isActive: false,
  errors: [],
  loading: false,
  payload: null
};

export function authReducer(state = initialState, action: AuthActions.AuthActions) {
  switch (action.type) {
    case(AuthActions.SIGN_IN):
    case(AuthActions.SIGN_OUT):
    
      return {
        ...state,
        loading: true
      };

    case (AuthActions.SIGN_IN_SUCCESS):
      let signInErrorClear = state.errors;
      for (let i = 0; i < signInErrorClear.length; i++) {
        if (signInErrorClear[i].errorEffect === AuthActions.SIGN_IN) {
          signInErrorClear = signInErrorClear.splice(i, 1);
        }
      }
      return {
        ...state,
        authenticated: true,
        errors: signInErrorClear,
        loading: false
      };
    case(AuthActions.AUTH_ERROR):
      let authErrorPush = state.errors;
      for (let i = 0; i < authErrorPush.length; i++) {
        if (authErrorPush[i].errorEffect === action.payload.errorEffect) {
          authErrorPush[i] = action.payload;
          return {
            ...state,
            errors: authErrorPush,
            loading: false
          };
        }
      }
      authErrorPush.push(action.payload);
      return {
        ...state,
        errors: authErrorPush,
        loading: false
      };

    case (AuthActions.SIGN_OUT_SUCCESS):
      return {
        authenticated: false,
        isActive: false,
        errors: [],
        loading: false, 
        payload: ''
      };
    case (AuthActions.CHECK_IF_LOGGED_IN):
      return {
        ...state,
        authenticated: true
      }  
    default:
      return state;
  }
}
