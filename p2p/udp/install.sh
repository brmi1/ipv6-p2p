#!/bin/bash

# Получаем название дистрибутива
dist=$(tr -s ' \011' '\012' < /etc/issue | head -n 1)

# Устанавливаем Miredo и добавляем в автозапуск
list_dist=(Ubuntu Debian Kali)

if [[ $list_dist[@] =~ $dist ]]; then
    apt-get install miredo
    systemctl enable miredo
    echo "Miredo is installed and added to autorun."
elif [[ "$dist" == "Fedora" ]]; then
    dnf install miredo
    systemctl enable miredo
    echo "Miredo is installed and added to autorun."
elif [[ "$dist" == "Manjaro" ]]; then
    sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf
    pamac install miredo
    systemctl enable miredo
    echo "Miredo is installed and added to autorun."
else
    echo "Miredo installation error. Perform the installation manually."
fi

# Имя нашего ipv6-интерфейса
IF_EXT="teredo"
# Сбрасываем все правила
ip6tables -F
# Разрешаем входящие пакеты
ip6tables -P INPUT ACCEPT
# Разрешаем исходящие пакеты
ip6tables -P OUTPUT ACCEPT

echo "The firewall is configured. Incoming packets are allowed."
# sudo /bin/sh install.sh