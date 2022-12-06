import Pessoa from './components/Pessoa';
// import logo from './logo.svg';
import './App.css';
import Counter from './hooks/UseState'

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Pessoa
          foto="https://avatars.githubusercontent.com/u/89954543?v=4"
          nome="André"
          idade="22"
          profissao="Developer"
        />

        <Counter></Counter>
      </header>
    </div >
  );
}

export default App;