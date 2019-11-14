from server import app


if __name__ == '__main__':
    print('Flask starting server...')
    app.run(
        host='127.0.0.1',
        port=3000,
        debug=True
    )


#Bash cmd to launch a serveo tunnel and keep it alive:
#ssh -o ServerAliveInterval=60 -R vivabot.serveo.net:80:localhost:3000 serveo.net

#Bash cmd to launch a ngrok tunnel
#ngrok http 300
