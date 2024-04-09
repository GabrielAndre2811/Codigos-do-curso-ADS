/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.gerenciabanco;
/**/


/**
 *
 * @author GABRIEL
 */




public class Conta {
    
    private static int countid = 1;
    private Integer idConta;
    Pessoa user;
    private Integer senha; // Senha de 6 dígitos
    private Double saldo = 0.0;
    
    public Conta(Pessoa user, Integer senha) {
        this.idConta = countid;
        this.user = user;
        this.senha = senha;
        this.updateSaldo();
        countid++;
    }

    public Integer getIdConta() {
        return idConta;
    }

    public void setIdConta(Integer idConta) {
        this.idConta = idConta;
    }

    public Pessoa getUser() {
        return user;
    }

    public void setUser(Pessoa user) {
        this.user = user;
    }

    public Integer getSenha() {
        return senha;
    }

    public void setSenha(Integer senha) {
        this.senha = senha;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }
    
    private void updateSaldo() {
        // Atualização do saldo
    }
    
    @Override
    public String toString() {
        return  "\nBank account: " + this.getIdConta() +
                "\nCliente: " + this.user.getNome()+ " " + this.user.getSobrenome() +
                "\nCPF: " + this.user.getCpf() +
                "\nEmail: " + this.user.getEmail() +
                "\nData de nascimento: " + this.user.getDatanascimento() +
                "\nSaldo: " + this.getSaldo() +
                "\n";
    }
    
    public String getNomeTitular() {
        return this.user.getNome() + " " + this.user.getSobrenome();
    }
    
    public void depositar(Double valor) {
        if (valor > 0) {
            setSaldo(getSaldo() + valor);
            System.out.println("Depósito realizado com sucesso!");
        } else {
            System.out.println("Valor inválido para depósito!");
        }
    }

    public void sacar(Double valor) {
        if (valor > 0 && this.getSaldo() >= valor) {
            setSaldo(getSaldo() - valor);
            System.out.println("Saque realizado com sucesso!");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido para saque!");
        }
    }

    public void transferencia(Conta contaDestino, Double valor) {
        if (valor > 0 && this.getSaldo() >= valor) {
            setSaldo(getSaldo() - valor);
            contaDestino.setSaldo(contaDestino.getSaldo() + valor);
            System.out.println("Transferência realizada com sucesso!");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido para transferência!");
        }
    }
}