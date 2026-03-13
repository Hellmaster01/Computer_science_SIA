#!/bin/bash
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка. Срипт запущен не от имени суперпользователя." >&2
    fi
}
check_root
