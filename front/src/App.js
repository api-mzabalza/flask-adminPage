import './App.css';
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';


// COMPONENTS
import Header from './components/Header/Header';
import Home from './components/Home/Home';
import Login from './pages/Login/Login';

// Redux
import { Provider } from 'react-redux';
import store from './store/store';
import setAuthToken from './utils/setAuthToken';


const App = () => {
  return (
    <Provider store={store}>
    <div>
      <div className='body'>
        <Header />

        <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
        </Switch>
        </BrowserRouter>
      </div>
    </div>
    </Provider>
  );
}

export default App;
