/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.gerenciabanco;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.InputMismatchException;


/**
 *
 * @author GABRIEL
 * 
 */


public class GerenciaBanco {   
    static Scanner input = new Scanner(System.in);
    static ArrayList<Conta> contasBancarias;
    public static void main(String[] args) throws IOException {
            try {            
            contasBancarias = new ArrayList<>();
            operacoes();
                
        } catch (InputMismatchException e) {
            System.out.println("Entrada inválida. Certifique-se de fornecer dados corretos.");
            operacoes();
        }
    }

    public static void operacoes() throws IOException {
        System.out.println("------------------------------------------------------");
        System.out.println("-------------Bem vindos a nossa Agência---------------");
        System.out.println("------------------------------------------------------");
        System.out.println("***** Selecione uma operação que deseja realizar *****");
        System.out.println("------------------------------------------------------");
        System.out.println("|   Opção 1 - Criar conta        |");
        System.out.println("|   Opção 2 - Acessar conta      |");
        System.out.println("|   Opção 3 - Extrato            |");
        System.out.println("|   Opção 4 - Sair do Sistema    |");
        System.out.println("------------------------------------------------------");

    int operacao = input.nextInt();

    switch (operacao) {
        case 1:
            criarConta();
            break;
        case 2:
            acessarConta();
            break;
        case 3:
            Extrato();
            break;
        case 4:
            System.out.println("Obrigado por usar nosso sistema!");
            System.exit(0); // para o sistema           
        case 996912377: 
            listarContas();
            break;
        default:
            System.out.println("Opção inválida!");
            operacoes();
            break;
    }    
    }

        public static void criarConta() throws InputMismatchException, IOException {
            System.out.println("Você está criando uma conta\n");
            
            input.nextLine();//limpa o buffer antes de iniciar para não pular a linha
            System.out.println("\nNome: (Nome Completo)");
            String nomeCompleto = input.nextLine().trim(); // Lê o nome completo com espaços e remove espaços extras
            
            
            String[] partesNome = nomeCompleto.split(" ");
            String nome = partesNome[0]; // Primeiro nome
            String sobrenome = ""; // Inicializa o sobrenome como vazio
            
            for (int i = 1; i < partesNome.length; i++) {
                sobrenome += partesNome[i]; // Concatena o sobrenome atual
                if (i < partesNome.length - 1) {
                    sobrenome += " "; // Adiciona um espaço se não for o último sobrenome
                }
            }
            
            
            System.out.println("\nCPF: (Formato: XXX.XXX.XXX-XX)");
            String cpf = input.next(); // Utilizamos next() para ler apenas uma palavra
            input.nextLine(); // Limpa o buffer de entrada

            System.out.println("\nEmail: ");
            String email = input.nextLine(); // Utilizamos nextLine() para permitir espaços em branco

            System.out.println("\nPor favor, digite sua data de nascimento (no formato DD/MM/AAAA): \n");
            String datanascimento = input.nextLine(); // Utilizamos nextLine() para permitir espaços em branco

            int senha = lerSenha();
            

            Pessoa user = new Pessoa(nome, sobrenome, cpf, email, datanascimento);
            Conta conta = new Conta(user, senha);

            contasBancarias.add(conta);

            System.out.println("------ Sua conta foi criada com sucesso! ------");
            System.out.println("Sua Conta é: " + conta.getIdConta());

            operacoes();
        }
     
     public static int lerSenha() throws InputMismatchException {
        System.out.println("\nDigite a senha para sua conta (6 dígitos): ");
        return input.nextInt(); // Ler a senha como um inteiro
    }

    
    
    public static void Extrato() throws IOException {
    System.out.println("Número da conta: ");
    int numeroConta = input.nextInt();
    System.out.println("Senha da conta: ");
    int senhaConta = input.nextInt();

    Conta conta = encontrarContaPorIdESenha(numeroConta, senhaConta);

    if (conta != null) {
        System.out.println("Informações da conta:");
        System.out.println(conta);
    } else {
        System.out.println("--- Conta não encontrada ou senha incorreta ---");
    }

    operacoes();
}
    
    public static void acessarConta() throws IOException {
        
    System.out.println("Número da conta: ");
    int numeroConta = input.nextInt();
    
    System.out.println("Senha: ");
    int senha = input.nextInt();
    

    Conta conta = encontrarContaPorIdESenha(numeroConta, senha);

    if (conta != null) {
       System.out.println("Seja Bem-Vindo: " + conta.user.getNome());
        // Conta encontrada com o número e senha corretos
        operacoesConta(conta);
    } else {
        
        System.out.println("Conta não encontrada ou senha incorreta!");
    
        operacoes();
    }
}
    
    public static void operacoesConta(Conta conta) throws IOException {
        System.out.println("------------------------------------------------------");
        System.out.println("-------------Operações disponíveis---------------------");
        System.out.println("------------------------------------------------------");
        System.out.println("|   Opção 1 - Depositar       |");
        System.out.println("|   Opção 2 - Sacar           |");
        System.out.println("|   Opção 3 - Transferir      |");
        System.out.println("|   Opção 4 - Dados Bancarios |");
        System.out.println("|   Opção 5 - Exibir Saldo    |");
        System.out.println("|   Opção 6 - Sair            |");
        System.out.println("------------------------------------------------------");

        int operacao = input.nextInt();

        switch (operacao) {
            
            case 1 -> depositar();

            case 2 -> sacar();

            case 3 -> transferir();
            
            case 4 -> Exibirdados(conta);

            case 5 -> exibirSaldo(conta);

            case 6 -> {
                System.out.println("Retornando ao menu principal...");
                operacoes();
            }

            default -> {
                System.out.println("Opção inválida!");
                operacoesConta(conta);
            }
        }
    }


    private static Conta encontrarConta(int numeroConta) { //somente usado para achar a conta do destinatario em caso de transferencia
        Conta conta = null;
        for(Conta cc : contasBancarias) {
            if(cc.getIdConta() == numeroConta) {
                conta = cc;
                break;
            }
        }
        return conta;
    }
    
    
    private static Conta encontrarContaPorIdESenha(int numeroConta, int senha) { //função que retorna a conta depois de procurar na classe contas usando idconta e senha como parametros
    Conta conta = null;
    for(Conta cc : contasBancarias) {
        if(cc.getIdConta() == numeroConta && cc.getSenha() == senha) {
            conta = cc;
            break;
        }
    }
    return conta;
}


public static void depositar() throws IOException {
    System.out.println("Número da conta: ");
    int numeroConta = input.nextInt();
    
    System.out.println("Senha da conta: ");
    int senha = input.nextInt();

    Conta conta = encontrarContaPorIdESenha(numeroConta, senha);

    if(conta != null) {
        System.out.println("Qual valor deseja depositar? ");
        double valorDeposito = input.nextDouble();

        conta.depositar(valorDeposito);
        System.out.println("--- Depósito realizado com sucesso! ---");
    } else {
        System.out.println("--- Conta não encontrada ou senha incorreta ---");
    }

    operacoesConta(conta);
}
    public static void exibirSaldo(Conta conta) throws IOException {
        
        System.out.println("Saldo atual da conta: " + conta.getSaldo());

        operacoesConta(conta); // Volta para as operações da conta
       
 
    }



    public static void sacar() throws IOException {
    System.out.println("Número da conta: ");
    int numeroConta = input.nextInt();
    
    System.out.println("Senha da conta: ");
    int senha = input.nextInt();

    Conta conta = encontrarContaPorIdESenha(numeroConta, senha);
    
    if(conta != null) {
        System.out.println("Qual valor deseja sacar? ");
        double valorSaque = input.nextDouble();

        if (conta.getSaldo() >= valorSaque) {
            conta.sacar(valorSaque);
            System.out.println("--- Saque realizado com sucesso! ---");
        } else {
            System.out.println("--- Saldo insuficiente ---");
        }
    } else {
        System.out.println("--- Conta não encontrada ou senha incorreta ---");
    }

    operacoesConta(conta);
}

    public static void transferir() throws IOException{
        System.out.println("Número da conta remetente: ");
        int numeroContaRemetente = input.nextInt();
        System.out.println("Senha da conta remetente: ");
        int senhaRemetente = input.nextInt();
    
        Conta contaRemetente = encontrarContaPorIdESenha(numeroContaRemetente, senhaRemetente);

        if (contaRemetente != null) {
            System.out.println("Número da conta destinatária: ");
            int numeroContaDestinatario = input.nextInt();
        
            Conta contaDestinatario = encontrarConta(numeroContaDestinatario);

            if (contaDestinatario != null) {
                System.out.println("Nome do destinatário: " + contaDestinatario.getNomeTitular());

                System.out.println("Você confirma que a conta " + numeroContaDestinatario + " é do destinatário? (sim/não)");
                String confirmacao = input.next();
            
             // Verifica a confirmação do usuário
                if ("sim".equalsIgnoreCase(confirmacao)) {
                    System.out.println("Valor da transferência: ");
                    double valorTransferencia = input.nextDouble();

                    if (contaRemetente.getSaldo() >= valorTransferencia) {
                        contaRemetente.transferencia(contaDestinatario, valorTransferencia);
                        System.out.println("--- Transferência realizada com sucesso! ---");
                    } else {
                        System.out.println("--- Saldo insuficiente para transferência ---");
                    }
                } else {
                    System.out.println("--- Transferência cancelada ---");
                }
            } else {
                System.out.println("--- Conta destinatária não encontrada ---");
            }

        } else {
            System.out.println("--- Conta remetente não encontrada ou senha incorreta ---");
        }

        operacoesConta(contaRemetente); // Volta para as operações da conta
    }

    public static void listarContas() throws IOException {
        if (contasBancarias.isEmpty()) {
            System.out.println("--- Não há contas cadastradas ---");
        } else {
            for (Conta conta : contasBancarias) {
                System.out.println(conta);
            }
        }
        operacoes();
    }
    
    public static void Exibirdados(Conta conta) throws IOException{
   
        System.out.println("\nCliente: " + conta.getNomeTitular() +
                           "\nConta do Banco: " + conta.getIdConta() +
                           "\nCPF: " + conta.user.getCpf() +
                           "\nEmail: " + conta.user.getEmail() +
                      "\nData de nascimento: " + conta.user.getDatanascimento()

                
                );
        
        System.out.println("*****Deseja editar dados da sua conta?   (sim/não)*****");
        String resposta = input.next();
        
        
        if ("sim".equals(resposta)){ 
            EditarConta();
        }else{
        
        operacoesConta(conta);
        }
        
    }
    
    public static void EditarConta() throws IOException {
    System.out.println("Número da conta: ");
    int numeroConta = input.nextInt();
    
    System.out.println("Senha da conta: ");
    int senha = input.nextInt();

    Conta conta = encontrarContaPorIdESenha(numeroConta, senha);

    if (conta != null) {
        System.out.println("------------------------------------------------------");
        System.out.println("------------\"Você está editando uma conta\"----------");
        System.out.println("------------------------------------------------------");
        System.out.println("***** Selecione uma operação que deseja realizar *****");
        System.out.println("------------------------------------------------------");
        System.out.println("|   Opção 1 - Editar Nome                    |");
        System.out.println("|   Opção 2 - Editar CPF                     |");
        System.out.println("|   Opção 3 - Editar Data de Nascimento      |");
        System.out.println("|   Opção 4 - Editar Email                   |");
        System.out.println("|   Opção 5 - Editar Senha                   |");
        System.out.println("|   Opção 6 - Excluir Conta                  |");
        System.out.println("|   Opção 7 - Sair                           |");
        System.out.println("------------------------------------------------------");

        int operacao = input.nextInt();

        switch (operacao) {
            case 1 -> {
                System.out.println("\nDigite o Novo Nome: (Completo) ");
                input.nextLine(); // Limpa o buffer
                String novoNomeCompleto = input.nextLine(); // Use nextLine() para ler a linha inteira
    
                String[] partesnovoNome = novoNomeCompleto.split(" ");
                String novoNome = partesnovoNome[0]; // Primeiro nome
                String novosobrenome = ""; // Inicializa o sobrenome como vazio

                for (int i = 1; i < partesnovoNome.length; i++) {
                    novosobrenome += partesnovoNome[i]; // Concatena o sobrenome atual
                    if (i < partesnovoNome.length - 1) {
                        novosobrenome += " "; // Adiciona um espaço se não for o último sobrenome
                    }
                }

    conta.user.setNome(novoNome);
    conta.user.setSobrenome(novosobrenome);

    System.out.println("------ Nome da conta foi editado com sucesso! ------");
    EditarConta();
    break;
}

            case 2 -> {
                System.out.println("\nNovo CPF: ");
                String novoCpf = input.next();
                conta.user.setCpf(novoCpf);
                System.out.println("------ CPF da conta foi editado com sucesso! ------");
                EditarConta();
                break;
            }

            case 3 -> {
                System.out.println("\nNova data de nascimento (no formato DD/MM/AAAA): ");
                String novaDataNascimento = input.next();
                conta.user.setDatanascimento(novaDataNascimento);
                System.out.println("------ Data de nascimento da conta foi editada com sucesso! ------");
                EditarConta();
                break;
            }

            case 4 -> {
                System.out.println("\nNovo email: ");
                String novoEmail = input.next();
                conta.user.setEmail(novoEmail);
                System.out.println("------ Email da conta foi editado com sucesso! ------");
                EditarConta();
                break;
            }

            case 5 -> {
                System.out.println("\nNova senha (6 dígitos): ");
                int novaSenha = input.nextInt();
                conta.setSenha(novaSenha);
                System.out.println("------ Senha da conta foi editada com sucesso! ------");
                EditarConta();
                break;
            }

            case 6 -> {
                System.out.println("------------------------------------------------------");
                System.out.println("****Atenção!!! - Deseja mesmo excluir sua conta?!*****");
                System.out.println("-----------------(sim ou não)-------------------------");
                System.out.println("------------------------------------------------------");
                String confirmacao = input.next();
                if ("sim".equalsIgnoreCase(confirmacao)) {
                    contasBancarias.remove(conta); // Remover a conta da lista de contas
                    System.out.println("--- Conta excluída com sucesso! ---");
                    operacoes();
                }else{
                    EditarConta();
                }
                break;
            }

            case 7 -> {
                System.out.println("Voltando ao menu anterior!");
                operacoesConta(conta);
                break;
            }

            default -> {
                System.out.println("Opção inválida!");
                EditarConta(); // Chamar recursivamente para fornecer outra chance de entrada válida
            }
        }
    } else {
        System.out.println("--- Conta não encontrada ou senha incorreta ---");
    }
}
    

    
}
    