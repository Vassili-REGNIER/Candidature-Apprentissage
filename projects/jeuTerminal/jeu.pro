TEMPLATE = app
CONFIG += console c++17
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
    code/source/game.cpp \
    code/source/gridmanagement.cpp \
    code/source/params.cpp \
    main.cpp

DISTFILES += \
    settings/settings.yaml \
    levels/l1.yaml \
    levels/l2.yaml \
    levels/l3.yaml \
    levels/l4.yaml \
    levels/l5.yaml \

HEADERS += \
    code/headers/game.h \
    code/headers/gridmanagement.h \
    code/headers/params.h \
    code/headers/type.h \
