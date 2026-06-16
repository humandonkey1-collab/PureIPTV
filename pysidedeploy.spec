[app]
# Название приложения на экране смартфона
title = PureIPTV Premium

# Уникальный ID (используется для установки обновлений)
package_name = org.pure.iptv.premium

# Версия приложения
version = 1.0.0

# Главный файл, с которого начинается запуск
entrypoint = main.py

# Какие файлы включить внутрь APK (скрипты, интерфейс, база данных)
include_files = main.py,main.qml,premium.db

# Список Python-библиотек, которые нужно упаковать
# Обязательно указываем requests и python-mpv
python_depends = requests,urllib3,idna,charset-normalizer,certifi,python-mpv

# Целевая платформа
target = android

# Архитектура (arm64-v8a — стандарт для современных смартфонов)
arch = arm64-v8a

[android]
# Разрешения для Android (Интернет — база для IPTV)
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Тема приложения (Fullscreen — на весь экран без рамок)
theme = @android:style/Theme.NoTitleBar.Fullscreen

# Скрывать навигационную панель при запуске
# hide_navigation = True
