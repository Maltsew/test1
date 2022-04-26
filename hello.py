def wsgi_application(environ, start_response):

    # основная логика WSGI приложения
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    #Дефолтный файл приложения подразумевает, что входной параметр будет один
    #а в тесте указано, что на вход подается группа параметров
    #в таком случае - генератор списка параметров
    #UPD: параметры передаеются в байтовом виде
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body
