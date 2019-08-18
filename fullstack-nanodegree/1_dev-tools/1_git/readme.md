# Git

- Tutorial:
https://www.udacity.com/course/version-control-with-git--ud123

- Git Cheatsheet by GitHub:
https://www.udacity.com/course/version-control-with-git--ud123

- Related Setup:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

- Referencia
https://git-scm.com/docs



## Configuracion inicial

```
git config --global user.name “Alejandro Martinez”
```
```
git config --global user.email “alemartineeez@gmail.com”
```
```
git config color.ui auto
```
```
git config core.editor “code --wait”
```
```
Actualizar .bash_profile
```


## Clonar repositorio
```
git clone https://github.com/GoogleChrome/lighthouse.git
```

**Historial de commits**
```
git shortlog -s -n
```
```
git show 5966b66
```
```
git log --author="Richard Kalehoff"
```
```
git log --grep="border radius issue in Safari"
```

**Resumen**
```
git log --oneline --graph --all
```

```
git shortlog -s -n
```
```
git log
```
Detallado
```
git log --stat
```

Muy detallado
```
git log -p
```

**Ultra Detallado**
```
git log -p --stat
```



## Add / Ignore
```
git add .
```
```
git reset --hard
```
```
git status
```
**Ignore**
```
vim .gitignore
```
```
/archivo.etx
```
```
git config --global core.excludesfile ~/.gitignore_global
```
**Eliminar**
```
git rm Hello.class
```


## Commit
```
git commit –m “description”
```
added pero no commit
```
git diff
```

## Tagging
```
git tag -a v1.0
```
Borrar tag
```
git tag -d v1.0
```
**Agregar tag a un commit anterior**
```
git tag -a v1.0 a87984
```

## Modificar Commits
```
git commit --amend
```
```
git revert a87984
```
```
git reset
```


## Branching
```
git branch
```
Crear branch
```
git branch sidebar
```
Cambiarse de branch
```
git checkout sidebar
```
**Crear y cambiar branch**
```
git checkout -b richards-branch-for-awesome-changes
```
Borrar branch
```
git branch -d sidebar
```

## Merging
Para hacer merge hay que estar parado en el branch que se desee combinar con otro
```
git merge sidebar
```

## Actualizar local desde el repo
```
git pull
```


## Subir una pagina a Github

1.	Crear repo desde la web de github.

2.	Copiar la URL

3.	Entrar al directorio con git

4.	Clonar (copiar los archivos existentes en el repositorio)
```
git clone +paste URL
```

5.	Si es una pagina vacia, copiar archivos dentro del repositorio

6.	git add
```
git add archivo.md
```
```
git status
```

7. Git Ignore
```
vim .gitignore
```
```
/archivo.etx
```

8.	Commit
```
git commit –m “description”
```

9.	Push
```
git push
```

10.	Todos los pasos anteriores

11.	Abrir las opciones del repo en github

12.	Habilitar Github Pages ✓



## Trabajar remotamente

1. Actualizar .bash_profile o .bashrc


2. Clonar repositorio
```
git clone https://github.com/GoogleChrome/lighthouse.git
```

3. Historial de commits

```
git shortlog -s -n
```

```
git show 5966b66
```

```
git log --author="Richard Kalehoff"
```

```
git log --grep="border radius issue in Safari"
```

4. Crear branch


5. Commit



## NPM live-server

Instalar NPM live-server
```
npm install –g live-server
```

Entrar al projecto
```
cd folder/project
```

Iniciar npm
```
live-server
```


## Authors

* **Alejandro Martinez** - *Initial work* - [CheatSheets for a Better Life](https://github.com/cheat-sheets)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
