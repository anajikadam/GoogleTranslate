import uvicorn

if __name__ == '__main__':
    uvicorn.run("app:app", 
    reload = True
    )

# if __name__ == '__main__':
#     uvicorn.run("app:app", port=5500, host='0.0.0.0',
#     reload = True, ssl_keyfile="SSL/key2.key", ssl_certfile="SSL/cert2.crt"
#     )


# if __name__ == '__main__':
#     uvicorn.run("app:app", port=8787, 
#     reload = True, 
#     ssl_keyfile="anajisslkey.key", ssl_certfile="anajisslpem.pem")