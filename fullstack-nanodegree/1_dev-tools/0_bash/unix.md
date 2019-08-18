# Unix Shell
- Referencia
https://superuser.com/questions/602872/how-do-i-modify-my-git-bash-profile-in-windows

## Navigation

**Goto directory**
```
cd path/etc/etc
```
**Move upwards**
```
cd ..
```

## Info

**ruta actual**
```
pwd
```
**Info de los archivos**
```
ls -l
```
**Desde afuera**
```
ls -l path/folder
```

## Operaciones

**Copiar**
```
cp path/origin path/destination
```
**Mover**
```
mv path/origin path/destination
```
**Borrar**
```
rm 'Bad File' 'Good File'
```
```
rm path/file.ext
```
**Borrar segun parametros**
```
rm *'Bad F'* 
```
**Borrar directorio**
```
rm -r path/folder
```
```
rmdir path/folder
```

## Más operaciones

**Descargar**
```
curl -L -o dictionary.txt 'https://tinyurl.com/zeyq9vc'
```

**Abrir archivo (visor)**
```
less file.txt
```
```
cat file.txt
```
**VIM**
```
vim file.ext
```
**Salir de VIM**
```
ESC + :wq
```

## Buscar
```
grep searchpattern dictionary.txt | less
```
**Contar matches**
```
grep searchpattern dictionary.txt | less | wc -l
```
**lo mismo pero desde un enlace**
```
curl -L 'https://tinyurl.com/zeyq9vc' | grep fish | wc -l
```

## Variables
**nueva variable**
```
numbers='one two three'
```
**mostrar**
```
echo $numbers
```
**Variables nativas**
```
echo $LINES x $COLUMNS
```
**add dir to path**
```
PATH=$PATH:new/dir/here
```

