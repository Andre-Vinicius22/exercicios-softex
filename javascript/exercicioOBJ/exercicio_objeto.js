function Banco(conta, saldo, tipoConta, agencia) {
    this.conta = conta;
    this.saldo = saldo;
    this.tipoConta = tipoConta;
    this.agencia = agencia;

    this.consultaSaldo = function () { console.log(`Seu saldo atual é de: R$${this.saldo}`) }
    this.deposito = function (deposito) {
        this.saldo = deposito + this.saldo
        console.log(`deposito de R$${deposito} realizado!`)
    }
    this.saque = function (saque) {
        this.saldo = this.saldo - saque
        console.log(`saque de R$${saque} realizado!`)
    }
    this.numeroConta = function () { console.log(`O numero da sua conta é: ${conta}`) }
}

var banco1 = new Banco('5120', 200, 'corrente', '0004')
banco1.consultaSaldo()
banco1.deposito(100)
banco1.consultaSaldo()
banco1.saque(50)
banco1.consultaSaldo()
banco1.numeroConta()