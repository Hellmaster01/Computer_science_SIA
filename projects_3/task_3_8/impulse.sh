#!/bin/bash
read -p "Имя гена: " name
read -p "Уровень экспрессии гена: " exp
if [[ -z "$name" ]] || [[ -z "$exp" ]]; then
    echo "Ошибка: недостаток входящих данных"
else
    echo "Экспрессия гена $name составляет $exp единиц"
fi
