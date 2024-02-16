#tuplas - Diccionarios

settings =('localhost',3306,'root','password','database')
print(settings)

print(len(settings))

host,port ,*_ =settings

print(host,port)

#Diccionarios

user ={
    'name':'cody',
    'age':'10',
    'email':'ema_fer_777@hotmail.com',
    'active': True
    
}

print(user)