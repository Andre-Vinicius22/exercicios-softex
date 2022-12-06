import "../App.css"

function Pessoa({ foto, nome, idade, profissao }) {

    return (
        <div className="person">
            <img src={foto} alt={nome} className="foto" />
            <p>Nome: {nome}</p>
            <p>Idade: {idade}</p>
            <p>Profissão: {profissao}</p>

            <div>
                Github:<a className="App-link" href="https://github.com/Andre-Vinicius22" target="_blank" rel="noopener noreferrer">
                    André Vinicius
                </a>
            </div>
        </div>
    )
}

export default Pessoa;