import React from "react";
import Header from "../components/header/Header";
import Pessoa from '../components/Pessoa';
import Counter from "../hooks/Counter";

function Home() {
    return(
        <div className="home">
                <Header/>
            <div className="home-content">

                <Pessoa foto="https://avatars.githubusercontent.com/u/89954543?v=4"
                    nome="André"
                    idade="22"
                    profissao="Developer"/>

                <Counter/>
            </div>
      </div>
    )
}

export default Home;