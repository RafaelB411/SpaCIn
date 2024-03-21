# SpaCIn Launch
O SpaCIN Launch é um jogo desenvolvido para a disciplina de Interface Hardware-Software. Nele, controlamos um foguete com os botões, switches e LEDs da placa de2i-150.

![SpaCIn game](/Screenshots/collage.jpg)

## Como rodar
1. Passe o mapeamento que está na pasta */map* para a placa utilizando o sofware Quartus;

Na pasta */driver/pci* :</br>
1. Rode o comando ```sudo insmod de2i-150.ko``` para adicionar o módulo;
3. Rode o comando ```sudo chmod 666 /dev/mydev``` para dar as permissões necessárias;

Na pasta */SpaCIn* :</br>
1. Rode o comando ```python3 main.py /dev/mydev``` para iniciar o jogo.

- [Comandos úteis](docs/commands.md)

## Como jogar
> Obs: Deixe todos os switches "para cima" antes começar a jogar
- Utilize os botões da placa para movimentar o foguete e desviar do lixo espacial. Se houver uma colisão, você perde o jogo;
- Os LEDs vermelhos da aplicação começam ligados. Sempre que uma fração do combustível acabar, o que é indicado na aplicação e com o desligamento de um LED, baixe o switch logo abaixo ao LED que apagou;
- A cada seis switches baixados, aperte o botão de desacoplamento para desacoplar uma parte do foguete;
- Você ganha o jogo quando desceu todos os switches e desacoplou os três módulos sem colidir com nenhum lixo espacial.