[app]
title = PureIPTV Premium
package.name = pureiptv
package.domain = org.humandonkey
source.dir = .
source.include_exts = py,qml,png,db
version = 2.0.0

# Все необходимые библиотеки для работы твоего Premium-плеера
requirements = python3,pyside6,requests,python-mpv,sqlite3

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Самая главная строчка, которая сама молча принимает лицензии Google вместо yes |
android.accept_sdk_license = True
