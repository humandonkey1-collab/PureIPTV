[app]
title = PureIPTV Premium
package_name = org.pure.iptv.premium
version = 1.0.0
entrypoint = main.py
input_file = main.py
# Включаем libmpv.so в сборку
include_files = main.py,main.qml,libmpv.so

[python]
python_depends = requests,urllib3,idna,charset-normalizer,certifi,python-mpv
android_packages = requests,urllib3,idna,charset-normalizer,certifi,python-mpv

[qt]
extra_modules = QtGui,QtQml,QtCore,QtQuick,QtLayouts

[android]
name = PureIPTV
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
theme = @android:style/Theme.NoTitleBar.Fullscreen
arch = arm64-v8a
# Указываем сборщику, что у нас есть нативная библиотека
extra_libs = libmpv.so
