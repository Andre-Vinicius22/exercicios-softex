import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          App criado para o primeiro exercicio de React para Softex.
        </p>
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
