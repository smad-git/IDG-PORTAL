import React from 'react';
import './App.scss';
import { BrowserRouter } from 'react-router-dom';
import { AppRouter } from './components/common/AppRouter';

function App() {
  return (
    <div className="App">
      <BrowserRouter basename={'patient-portal'}>
        <AppRouter/>
      </BrowserRouter>
    </div>
  );
}

export default App;
