# citizencard_odoo
Read portuguese citizen card using Python and odoo external API

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
- Esta aplicação foi testada com o WINDOWS 10 e com o leitor de cartões da GEMALTO!
- Para aceder à morada é necessário um PIN que por default é 0000. Caso o cartão tenha este PIN ou não se encontre bloqueado, a aplicação lê automaticamente a morada. Caso contrário, processa a restante informação.

Os elementos transferidos são:
- Dados pessoais;
- Morada (caso o PIN seja 0000);
- Fotografia.
