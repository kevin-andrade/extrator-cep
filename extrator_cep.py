import re  # Regular Expression -- RegEx

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 dígitos + hífen (opcional) + 3 dígitos
#padrao  = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

# Quantificadores e intervalos
# Usa Hífen para fazer o itervalo, dizer que contém de 0 a 9 digítos dentro desse caractere. Pode ser feito com letras [a-b]
# Quantificadores {} irá conter 5 caracteres daquele tipo, {0,1} poderá conter de 0 a 1.
padrao  = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Pesquisar na variavel o padrão, cria um objeto Match
if busca:
    cep = busca.group() # Group recebe o valor retornado por Match
    print(cep)