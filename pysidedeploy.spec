[app]
title = PureIPTV Premium
package_name = org.pure.iptv.premium
version = 1.0.0
entrypoint = main.py
# Файлы, которые будут упакованы
include_files = main.py,main.qml,libmpv.so

[python]
# Ключ, который ищет сборщик 6.8.0 для установки зависимостей внутри Android
android_packages = requests,urllib3,idna,charset-normalizer,certifi,python-mpv,buildozer,cython
# Для обратной совместимости
python_depends = requests,urllib3,idna,charset-normalizer,certifi,python-mpv

[qt]
# Модули, которые линтер должен включить принудительно
modules = Core,Gui,Qml,Quick,Layouts,Multimedia

[buildozer]
# ВОТ ОНО! Исправляет TypeError: ... not NoneType
mode = release
# Архитектура для современных телефонов
arch = aarch64
# Путь к нативным либам внутри APK
local_libs = libmpv.so

[android]
# Метаданные для системы Android
name = PureIPTV
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
theme = @android:style/Theme.NoTitleBar.Fullscreen
