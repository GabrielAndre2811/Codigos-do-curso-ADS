/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.gerenciabanco;

/**
 *
 * @author GABRIEL
 */

public class Pessoa {
    
    private String nome;
    private String sobrenome;
    private String cpf;
    private String email;
    private String datanascimento;

    public Pessoa(String nome, String sobrenome, String cpf, String email, String datanascimento) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.email = email;
        this.datanascimento = datanascimento;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }
      
    public String getSobrenome() {
        return sobrenome;
    }
    
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getDatanascimento() {
        return datanascimento;
    }

    public void setDatanascimento(String datanascimento) {
        this.datanascimento = datanascimento;
    }
    
 
    @Override
    public String toString() {
        return "\nNome: " + this.getNome() + " " + this.getSobrenome() + // Adiciona um espaço entre o nome e o sobrenome
                "\nCPF: " + this.getCpf() +
                "\nEmail: " + this.getEmail() +
                "\nData de Nascimento: " + this.getDatanascimento();
    }
}