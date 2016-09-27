
def app(environ, start_response):

    string = environ['PATH_INFO'][1:]
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)

    if string.find("hello.html") != -1:

        return 'Hello lala!\n'
        
    elif string.find(".html") != -1:

        return '404 Not Found'

    else:
        
        return 'Hello, %s!' % (environ['PATH_INFO'][1:] or 'web')
        
