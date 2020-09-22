# Personalização dos manuais de ajuda do Helios

Esse manual de ajuda foi feito com [MkDocs](http://www.mkdocs.org/) e com o tema
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) com algumas
pequenas adaptações no CSS. 

Caso deseje alterar o texto do manual, basta editar os arquivos presentes no
diretório [docs](docs/).

Caso queira customizar o CSS, edite o arquivo [extra.css](docs/stylesheets/extra.css).

Após as alterações será necessário compilar, fazendo uso do comando `mkdocs build`. 

Os arquivos resultantes da compilação serão armazenados no diretório `site`.
Mova esses arquivos para dentro do diretório que está mapeando no Apache para
hospedar a página de ajuda.
