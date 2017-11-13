# citizencard_odoo
Read portuguese citizen card based on Python and post data using odoo external API
Any additional question please contact me by email: pedroposeiro@gmail.com

## IN ENGLISH:

## To install the app:

1) Install drivers for the reader (GemPcCCID for Gemalto reader)

2) Insert "cartao_cc" folder anywhere in the c: drive.

## To startup with windows:

3) Create a shortcut from the "cartao_cc.exe" file and then copy this file

4) Open Run from start and type: *shell:startup*

5) Paste the copied file into the startup window

6) Restart PC and wait up to appear a popup to insert card into the reader. All the process is automatic.

## Credentials to access odoo VM:

http://odoo9-cartaocidadao-pedroposeiro.c9users.io

Username: *demo*

Password: *demo*

## Notes:
- To access the address you need to use the PIN code, by defaul is 0000. If this PIN is does not have been changed or the card is not blocked, this app read the address automatically. Otherwise, only all free available information is transfered.

## Data transfered by the card:
- [x] Personal data;
- [x] Address (if PIN by default is 0000);
- [x] Photo.

## Test compatibility:
### OS Test
- [x] WINDOWS 10 
- [x] WINDOWS 7 (Popups is not working)

### Odoo version
- [x] ODOO 9

### Card Reader
- [x] Gemalto GemPC Twin USB
- [x] HP USB Smartcard CCID Keyboard

## EM PORTUGUÊS:

## Para instalar a aplicação:

1) Instalar drivers do leitor de cartões (GemPcCCID no caso do leitor da Gemalto)

2) Inserir a pasta "cartao_cc" em qualquer local no disco c:

## Para arrancar a aplicação com o windows:

3) Criar um ficheiro de atalho do ficheiro "cartao_cc.exe" e depois cortar/copiar esse ficheiro (cartao_cc - Shortcut)

4) Abrir a janela Run (Executar) no iniciar e escrever: *shell:startup*

5) Colar o ficheiro de atalho na janela que abriu

6) Reiniciar o PC e esperar que apareça um popup a dizer que pode inserir um cartão no leitor. Todo o restante processo é automático.

## Credenciais de acesso ao odoo:

http://odoo9-cartaocidadao-pedroposeiro.c9users.io

Username: *demo*

Password: *demo*

## Notas:
- Para aceder à morada é necessário um PIN que por default é 0000. Caso o cartão tenha este PIN ou não se encontre bloqueado, a aplicação lê automaticamente a morada. Caso contrário, processa a restante informação.

## Os elementos transferidos são:
- [x] Dados pessoais;
- [x] Morada (caso o PIN seja 0000);
- [x] Fotografia.

## Teste de compatibilidade:
### Sistema operativo
- [x] WINDOWS 10 
- [x] WINDOWS 7 (Popups is not working)

### Odoo versão
- [x] ODOO 9

### Leitor de cartões
- [x] Gemalto GemPC Twin USB
- [x] HP USB Smartcard CCID Keyboard
