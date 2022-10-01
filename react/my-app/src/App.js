import Header from './components/Header';
import logo from './logo.svg';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <Header></Header>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://github.com/Andre-Vinicius22"
          target="_blank"
          rel="noopener noreferrer"
        >
          Github: André Vinicius
        </a>

        <p> Turma do Instrutor Danilo - turno noite</p>
      </header>
    </div>
  );
}

export default App;
