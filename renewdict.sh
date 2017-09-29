#!/bin/sh
# NOT BASH ==> echo -e doesn't need !

echo ""

CNORM="\033[0m"
CRED="\033[31m"
CSRC="\033[35m"
CDST="\033[36m"
CTRAITED="\033[1;33m"

dict='dict.sqlite'

src='/home/will/.mozilla/firefox/g37dpyv5.default/extensions/rikaichan-jpfr@polarcloud.com/'$dict
dst='/home/will/data/programmation/python/shiri-tori/'$dict

echo "Copie de \n\t"$CSRC$src$CNORM"\nvers\n\t"$CDST$dst$CNORM

if [ -f $dst ]; then
   echo "\n$CRED Fichier $dict éxistant : copie en $dict.old$CNORM"
   old=$dst.old
   cp -p $dst $old
fi

echo ""

cp -pv $src $dst

echo ""

#echo "Nombre de champs traités :"$CTRAITED $(jshon -l < items.json)"$CNORM\n\n"
