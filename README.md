# PythonGreenAtom
Добрый день! Для запуска прилодения нужно будет установить все зависимости в файле requaruments.txt, а также скачать minio, затем запустить minio 
командой minio.exe server "путь до папки с гита\sever\bucks" --console-address ":9001". Далее небъодимо запустить файл main.py командой uvicorn main:app --reload.
Сервер должен по умолчанию запуститься по адрессу http://127.0.0.1:8000. Это важно, так как программа тестирования подключается имено по этому адрессу.
Чтобы выполнить тесты нужно просто запустить файл, выполняющий тесты. 
