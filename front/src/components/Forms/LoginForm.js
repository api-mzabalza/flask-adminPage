import React, { useState, useEffect } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import './Form.scss';

// Components
// import SubmitButton from '../Button/SubmitButton';

// Actions
import { login } from '../../store/actions/auth';

const Form = ({ isAuthenticated, login }) => {


    const [formData, setFormData] = useState({
        // email: '',
        // password: ''
    });

    const { email, password } = formData;


    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
    const onSubmit = async e => {
        e.preventDefault();
        console.log(email, password);
        login(email, password);
    };


    if (isAuthenticated) {
        console.log('redirect');
        return <Redirect to='/home' />
    }


    return (
        <div>
            <div className='flex-row-sa my-2 users-icon'>
                <i class="fas fa-users"></i>
            </div>

            <div className='form-title'>
                <h1>MEMBER LOGIN</h1>

            </div>

            <form className='form' onSubmit={(e) => onSubmit(e)}>
                <div className="form-group">
                    <input type='text' name='email' placeholder='username' autoComplete="off" onChange={e => onChange(e)} />
                </div>
                <div className="form-group">
                    <input type="password" name='password' placeholder='password' autoComplete="off" onChange={e => onChange(e)} />
                </div>
                <div className='flex-row-sa my-2'>
                    <div onClick={onSubmit}></div>
                </div>
            </form>


        </div>

    )
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { login })(Form);