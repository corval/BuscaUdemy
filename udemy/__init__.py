# UdemyBot - A Simple Udemy Free Courses Scrapper

# Copyright (C) 2021-Present Gautam Kumar <https://github.com/gautamajay52>

import os

token = os.environ.get('TOKEN')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

START = """
Hola Soy un Bot para Udemy. ⚡

Puedo conseguirte cursos gratis en Udemy.

Commandos:
    Página /discudemy
    Página /udemy_freebies
    Página /tutorialbar
    Página /real_discount
    /coursevania
    Página /idcoupons

página: qué página quería desechar y enviar enlaces. El valor predeterminado es 1
"""

CMD = "(discudemy|coursevania|udemy_freebies|tutorialbar|real_discount|idcoupons)"
