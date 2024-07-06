import hashlib
def hash_teste(criar_hash,tipo_hash='md5'):
        tipo_hash.encode('utf-8')
        m = hashlib.new(tipo_hash)
        m.update(criar_hash)
        return m.hexdigest()
    

def quebrarHash(hashpronto, tipo_hash):
    
    arq = open("rockyou.txt", 'r', encoding='utf-8' )
    cont = 0
    if tipo_hash == '1':
        hashlib1 = hashlib.sha512
    if tipo_hash == '2':
        hashlib1 = hashlib.md5
    if tipo_hash == '3':
        hashlib1 = hashlib.sha256
    if tipo_hash == '4':
        hashlib1 = hashlib.sha3_512
    if tipo_hash == '5':
        hashlib1 = hashlib.sha1
    if tipo_hash == '6':
        hashlib1 = hashlib.shake_256
    if tipo_hash == '7':
        hashlib1 = hashlib.blake2b
    if tipo_hash == '8':
        hashlib1 = hashlib.sha224
    else:
        print('Opção invalida!!!!!!')
        
    for item in arq:
        temp = hashlib1(item.rstrip().encode('utf-8')).hexdigest()
        if hashpronto == temp:
            print(f"Valor da hash informado: {hashpronto}.\nHash encontrado: {temp}.\nSenha:{item}\nNa linha:{cont}.")
            break
        cont += 1
        
    
        
    
print("-"*10, "Bem vindo","-"*10)
opcao = int(input("""Digite quais das opcoes voce quer:
[1] Comparador de hash
[2] Criar hash
[3] brute force
: """))
if opcao == 1:
    hash1 = str(input("Digite o primeiro hash a ser comparada: "))
    hash2 = str(input("Digite a segunda hash a ser comparada: "))
    if hash1 == hash2:
        print(f"Primero hash digitado: {hash1}")
        print(f"segundo hash digitado: {hash2}")
        print("Sao iguais")
    else:
        print(f"Primero hash digitado: {hash1}")
        print(f"segundo hash digitado: {hash2}")
        print("Nao Sao iguais")
if opcao == 2:
    
    criar_hash = str(input("Digite o texto que quer criar a hash: ")).encode('utf-8')
    tipo_hash = str(input("""Digite qual tipo de hash vai escolher
[shaw512, md5, sha256 ,sha3_512, sha1, shake_256, blake2b, sha224]. 
Digite tudo em minusculo, se nada for digitado sera feito em md5: """))
    total = hash_teste(criar_hash,tipo_hash)
    print(total)
if opcao == 3:
    
    hashpronto = str(input('Digite o hash que deseja quebrar: '))
    tipo_hash = str(input("""Digite qual tipo de hash vai escolher
[[1]shaw512, [2]md5, [3]sha256 ,[4]sha3_512, [5]sha1, [6]shake_256, [7]blake2b, [8]sha224]. 
Digite tudo em minusculo, se nada for digitado sera feito em md5: """))     
    total1 = quebrarHash(hashpronto,tipo_hash)

