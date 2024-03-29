import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import About from './pages/about/About';

const App = () => {
  return (
      <Router>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/about' element={<About/>}/>
        </Routes>
      </Router>
  );
}

export default App;