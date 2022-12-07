import Pessoa from './components/Pessoa';
// import logo from './logo.svg';
import './App.css';
import Counter from './hooks/Counter'

const App = () => {
  return (
    <div className="App">
      <div className="App-content">
        <Pessoa
          foto="https://avatars.githubusercontent.com/u/89954543?v=4"
          nome="André"
          idade="22"
          profissao="Developer"
        />

        <Counter></Counter>
        
      </div>
    </div>
  );
}

export default App;