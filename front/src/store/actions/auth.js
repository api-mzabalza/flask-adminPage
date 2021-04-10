import axios from 'axios';
import setAuthToken from '../../utils/setAuthToken';


import { setAlert } from './alert';
import { LOGIN_SUCCESS, LOGOUT, LOGIN_FAIL, USER_LOADED, AUTH_ERROR, REGISTER_SUCCESS, REGISTER_FAIL } from '../actions/types';

// Load User
export const loadUser = () => async dispatch => {
    console.log(localStorage.token);
    if (localStorage.token) {
        setAuthToken(localStorage.token)
    }
    try {
        const res = await axios.get('/api/token');
        dispatch({
            type: USER_LOADED,
            payload: res.data
        });
    } catch (err) {
        console.log(err);
        dispatch({
            type: AUTH_ERROR
        });
    }
}


export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    }
    const body = JSON.stringify({ email, password });
    console.log('trying Request');
    try {
        const resp = await axios.post(`/api/login`, body, config);
        dispatch({
            type: LOGIN_SUCCESS,
            payload: resp.data
        });

        dispatch(loadUser());
    } catch (err) {
        const error = err.response.data.message;

        if (err) {
            dispatch(setAlert(error, 'danger'));
        }
        dispatch({
            type: LOGIN_FAIL,
        });
    }
};

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    })
};

export const register = (user) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    }
    const body = JSON.stringify(user);
    try {
        const resp = await axios.post(`/api/users`, body, config);
        dispatch({
            type: REGISTER_SUCCESS,
            payload: resp.data
        })

    } catch (err) {
        const error = err.response.data.message;
        if (err) {
            dispatch(setAlert(error, 'danger'));
        }
        dispatch({
            type: REGISTER_FAIL
        })
    }

};