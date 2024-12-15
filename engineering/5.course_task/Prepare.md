По традиции сначала подготовим окружение:

Для того чтобы обращаться к модулю мониторинга используемых услуг, нужно проделать следующие шаги:

Перейти в наш репозиторий на GitLab
Перейти в директорию модуля 3.Client_modules
В директории final_practice_helpers вас будут ждать несколько файлов
Все эти файлы необходимо перенести к себе на локальную машину и перейти в директорию с ними.
Далее, при помощи утилиты docker-compose необходимо создать окружение. Это можно сделать командой
 docker-compose -f docker-compose.yaml up -d --build

После запуска вам будет доступна СУБД postgresql и opessh-server
Для postgresql также доступен веб-интерфейс по адресу
http://localhost:8080/
Credentials СУБД:
host: localhost (если подключаетесь через веб-интерфейс, то вводим postgres) 
user: postgres
password: q1w2e3
database: postgres
schema: usage_stats
Credentials openssh-сервера:
host: localhost
port: 2222
user: service_user
password: q1w2e3

При запуске команды с openssh-сервера:
monitoring_module <seed>
где seed целое число, в базу данных (в таблицу resources) будут сгенерированы те же метрики, что отдавались модулем мониторинга по обращению через HTTP.
Схема данных в таблице представлена полями:
team - Название команды,
resource - ID ресурса, 
dimension - Измерение ресурса (CPU, RAM или NetFlow)
collect_date - Дата и время сбора статистики
usage - Загрузка ресурса в процентах (от 0 до 100)
После выполнения важно не забыть отключить ресурсоёмкое окружение при помощи команды
docker-compose down