# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import requests
import unicodedata
from time import sleep

from selenium import webdriver

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "AcceptAlert":

    web = GetGlobals('web')
    driver = web.driver_list[web.driver_actual_id]

    option = GetParams("option")
    content = GetParams("content")
    res_ = GetParams("res_")

    try:
        alert = driver.switch_to.alert

        if res_:
            tmp = unicodedata.normalize('NFKD', alert.text).encode("ascii", "ignore").decode()
            SetVar(res_, tmp)

        if content:
            print('cont', content)
            try:
                alert.send_keys(content)
                sleep(5)
            except:
                PrintException()

        if option == "confirm":
            alert.accept()
        else:
            alert.dismiss()

    except:
        PrintException()


if module == "waitAlert":
    import time

    web = GetGlobals('web')
    driver = web.driver_list[web.driver_actual_id]

    var = True
    seg_ = int(GetParams('seg_'))
    var_ = GetParams('var_')
    not_show_exeption_ = GetParams('not_show_exeption_')
    cont = 1
    res_ = ""

    while var and cont <= seg_:
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            var = False
            res_ = True
        except:
            if not not_show_exeption_:
                PrintException()
            cont += 1
            res_ = False
            continue

    SetVar(var_, res_)