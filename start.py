import subprocess
import time
import os

while True:
    # Запуск скриптов в новом процессе
    print('Запуск main.py')
    m = subprocess.Popen(['python3', 'main.py'])

    # Ждем 6 часов
    time.sleep(6 * 30 * 30) # 6 часов в секундах
    
    # Завершаем процесс, в котором запущен main.py
    print('Завершаем процесс main.py')
    m.terminate()
    m.wait()  # Дожидаемся завершения процесса

    time.sleep(5)
    # Запускаем main.py снова
    print('Запускаем заново')
