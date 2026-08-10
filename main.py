#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os

# Порт, на котором будет работать сервер (можно изменить)
PORT = 8000

# Переключаемся в директорию со скриптом, чтобы файлы искались рядом
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Обработчик запросов – стандартный для статики
Handler = http.server.SimpleHTTPRequestHandler

# Запускаем сервер
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    print(f"Откройте в браузере: http://localhost:{PORT}")
    print("Нажмите Ctrl+C для остановки")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")