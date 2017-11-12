# citizencard_odoo
Read portuguese citizen card based on Python and post data using odoo external API

IN ENGLISH:

To install the app:

1) Install drivers for the reader (GemPcCCID for Gemalto reader)

2) Insert "cartao_cc" folder anywhere in the c: drive.

To startup with windows:

3) Create a shortcut from the "cartao_cc.exe" file and then copy this file

4) Open Run from start and type: shell:startup

5) Paste the copied file into the startup window

6) Restart PC and wait up to appear a popup to insert card into the reader. All the process is automatic.

Credentials to access odoo VM:

http://odoo9-cartaocidadao-pedroposeiro.c9users.io

Username: demo

Password: demo

Notes:
- This app was tested for WINDOWS 10 and, for the GEMALTO card reader and for odoo 9!
- To access the address you need to use the PIN code, by defaul is 0000. If this PIN is does not have been changed or the card is not blocked, this app read the address automatically. Otherwise, only all free available information is transfered.

Data transfered by the card:
- Personal data;
- Address (if PIN by default is 0000);
- Photo.


EM PORTUGUÊS:

Para instalar a aplicação:

1) Instalar drivers do leitor de cartões (GemPcCCID no caso do leitor da Gemalto)

2) Inserir a pasta "cartao_cc" em qualquer local no disco c:

Para arrancar a aplicação com o windows:

3) Criar um ficheiro de atalho do ficheiro "cartao_cc.exe" e depois cortar/copiar esse ficheiro (cartao_cc - Shortcut)

4) Abrir a janela Run (Executar) no iniciar e escrever: shell:startup

5) Colar o ficheiro de atalho na janela que abriu

6) Reiniciar o PC e esperar que apareça um popup a dizer que pode inserir um cartão no leitor. Todo o restante processo é automático.

Credenciais de acesso ao odoo:

http://odoo9-cartaocidadao-pedroposeiro.c9users.io

Username: demo

Password: demo

Notas:
- Esta aplicação foi testada com o WINDOWS 10, com o leitor de cartões da GEMALTO e para o odoo 9!
- Para aceder à morada é necessário um PIN que por default é 0000. Caso o cartão tenha este PIN ou não se encontre bloqueado, a aplicação lê automaticamente a morada. Caso contrário, processa a restante informação.

Os elementos transferidos são:
- Dados pessoais;
- Morada (caso o PIN seja 0000);
- Fotografia.

Any additional question please contact me by email: pedroposeiro@gmail.com
