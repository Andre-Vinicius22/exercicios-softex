// para rodar o projeto necessario instalar o "ts-node" atraves do "NPM".

class Veiculo {
    constructor(
        public rodas: Number,
        public peso: Number,
        public passageiros: Number
    ) { }
}

let Veiculo_1: Veiculo;
Veiculo_1 = new Veiculo(2, 700, 2)

let Veiculo_2: Veiculo;
Veiculo_2 = new Veiculo(4, 2500, 5)

let Veiculo_3: Veiculo;
Veiculo_3 = new Veiculo(4, 5000, 3)

let Veiculo_4: Veiculo;
Veiculo_4 = new Veiculo(4, 7000, 12)

let Veiculo_5: Veiculo;
Veiculo_5 = new Veiculo(6, 10000, 3)

function Habilitacao(veiculo: Veiculo) {
    if (veiculo.rodas == 2) {
        return console.log("sugerimos a habilatacao A");
    } if (veiculo.rodas == 4 && veiculo.peso <= 3500 && veiculo.passageiros <= 8) {
        return console.log("sugerimos a habilitacao B");
    } if (veiculo.rodas >= 4 && veiculo.peso >= 3500 && veiculo.peso <= 6000) {
        return console.log("sugerimos a habilitacao C");
    } if (veiculo.rodas >= 4 && veiculo.passageiros > 8) {
        return console.log("sugerimos a habilitacao D");
    } if (veiculo.rodas >= 4 && veiculo.peso > 6000) {
        return console.log("sugerimos a habilitacao E");
    }
}

Habilitacao(Veiculo_1);
Habilitacao(Veiculo_2);
Habilitacao(Veiculo_3);
Habilitacao(Veiculo_4);
Habilitacao(Veiculo_5);