# Enunciado
## Somador on/off
Somador on/off: criar o programa em Python
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.


Explicação do código realizado por mim:
A minha lógica para este código tratou de, num primeiro passo, eliminar as sequências de texto entre 'off' e 'on' e remover as mudanças de linha. Seguidamente, vou percorrendo carater a carater do texto resultante e juntando as sequências de dígitos que formam números inteiros a somar. Quando ocorre um '=', aparece o resultado da soma até aquele momento.
O único erro que não estou a conseguir resolver é se no final do texto aparecer 'Off' mas não voltar a aparecer 'on'. Não percebo porque esta expressão regular não funciona: '(OFF).*?(ON?|$)'
