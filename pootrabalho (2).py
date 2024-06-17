lista_medicos = []
lista_pacientes = []
lista_convenios = []
lista_consultas = []
lista_compromissos = []

def cadastrarMedicos():
    Medico_Nome = input('Nome do Médico: ')
    Medico_CPF = input('Digite o CPF: ')
    Medico_RG = input('Digite o RG: ')
    Medico_CRM = input('Digite o CRM: ')
    Medico_Telefone = input('Telefone do Médico: ')
    Medico_Endereco = input('Endereço do Médico: ')
    Medico_Sexo = input('Sexo: ')
    Medico_Senha = input('Digite a senha de acesso: ')
    lista_medicos.append({
        'nome': Medico_Nome,
        'CPF': Medico_CPF,
        'RG': Medico_RG,
        'CRM': Medico_CRM,
        'telefone': Medico_Telefone,
        'endereco': Medico_Endereco,
        'sexo': Medico_Sexo,
        'senha': Medico_Senha
    })
    print('Médico Cadastrado')

def cadastrarPacientes():
    Paciente_Nome = input('Nome do Paciente: ')
    Paciente_CPF = input('Digite o CPF: ')
    Paciente_RG = input('Digite o RG: ')
    Paciente_Telefone = input('Telefone do Paciente: ')
    Paciente_Endereco = input('Endereço do Paciente: ')
    Paciente_Sexo = input('Sexo: ')
    Paciente_Senha = input('Digite a senha de acesso: ')
    lista_pacientes.append({
        'nome': Paciente_Nome,
        'CPF': Paciente_CPF,
        'RG': Paciente_RG,
        'telefone': Paciente_Telefone,
        'endereco': Paciente_Endereco,
        'sexo': Paciente_Sexo,
        'senha': Paciente_Senha
    })
    print('Paciente Cadastrado')

def cadastrarConvenios():
    Convenios_nome = input('Nome do Convênio:')
    Convenios_CNPJ = input('Digite o CNPJ:')
    Convenios_telefone = input('Telefone do Convênio:')
    Convenios_endereco = input('Endereço do Convênio:')
    Convenios_Senha = input('Digite a senha de acesso:')
    lista_convenios.append({
        'nome': Convenios_nome,
        'CRM': Convenios_CNPJ,
        'telefone': Convenios_telefone,
        'endereco': Convenios_endereco,
        'senha': Convenios_Senha
    })
    print('Convênio Cadastrado')

def marcarCompromisso():
    print("Marcar Compromisso")
    medico = buscarMedicos()
    if not medico:
        print("Médico não encontrado.")
        return
    
    paciente = buscarPacientes()
    if not paciente:
        print("Paciente não encontrado.")
        return
    
    data = input("Agendar a data do compromisso: ")
    horario = input("Horário do compromisso: ")
    
    lista_compromissos.append({
        'medico': medico['nome'],
        'paciente': paciente['nome'],
        'data': data,
        'horario': horario
    })
    print("Compromisso agendado!.")



def buscarMedicos():
    busca = input("Deseja procurar médico pelo nome ou CRM? ")
    
    if busca == "nome":
       
        nome = input("Digite o nome do médico: ")
        
        for medico in lista_medicos:
            
            if medico['nome'] == nome:
                print(medico)
                
                return medico
       
        print("Médico não encontrado.")
   
    elif busca == "crm":
        
        crm = input("Digite o CRM do médico: ")
        
        for medico in lista_medicos:
           
            if medico['CRM'] == crm:
                
                print(medico)
               
                return medico
        print("Médico não encontrado.")
    else:
        print("Busca inválido.")

def buscarPacientes():
    busca = input("Deseja procurar paciente pelo nome ou CPF? ")
    if busca == "nome":
        
        nome = input("Digite o nome do paciente: ")
        
        for paciente in lista_pacientes:
            if paciente['nome'] == nome:
               
                print(paciente)
                
                return paciente
        print("Paciente não encontrado.")
    
    elif busca == "cpf":
       
        cpf = input("Digite o CPF do paciente: ")
        
        for paciente in lista_pacientes:
           
            if paciente['CPF'] == cpf:
                print(paciente)
               
                return paciente
        print("Paciente não encontrado.")
    else:
        print("Busca inválido.")

def buscarConvenios():
    busca = input("Deseja buscar convênio por nome ou CNPJ? ")
    
    if busca == "nome":
        nome = input("Digite o nome do convênio: ")
       
        for convenio in lista_convenios:
           
            if convenio['nome'] == nome:
                print(convenio)
                return convenio
        
        print("Convênio não encontrado.")
    
    elif busca == "cnpj":
        cnpj = input("Digite o CNPJ do convênio: ")
        
        for convenio in lista_convenios:
            if convenio['CNPJ'] == cnpj:
                print(convenio)
                return convenio
        print("Convênio não encontrado.")
    else:
        print("Critério inválido.")

def alterarMedicos():
    medico = buscarMedicos()
   
    if medico:
        print("Alterar os dados do médicos:")
        nome = input(f"Nome {medico['nome']}: ")
        CPF = input(f"CPF ({medico['CPF']}): ")
        RG = input(f"RG ({medico['RG']}): ")
        CRM = input(f"CRM ({medico['CRM']}): ")
        telefone = input(f"Telefone ({medico['telefone']}): ")
        endereco = input(f"Endereço ({medico['endereco']}): ")
        sexo = input(f"Sexo ({medico['sexo']}): ")
        senha = input(f"Senha ({medico['senha']}): ")

        medico.mudar({
            'nome': nome,
            'CPF': CPF,
            'RG': RG,
            'CRM': CRM,
            'telefone': telefone,
            'endereco': endereco,
            'sexo': sexo,
            'senha': senha
        })
        print("Dados do médico foram alterados!")

def alterarPacientes():
    paciente = buscarPacientes()
    if paciente:
        print("Altere os dados do paciente. Deixe em branco para manter o valor atual.")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        CPF = input(f"CPF ({paciente['CPF']}): ") or paciente['CPF']
        RG = input(f"RG ({paciente['RG']}): ") or paciente['RG']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        senha = input(f"Senha ({paciente['senha']}): ") or paciente['senha']

        paciente.mudar({
            'nome': nome,
            'CPF': CPF,
            'RG': RG,
            'telefone': telefone,
            'endereco': endereco,
            'sexo': sexo,
            'senha': senha
        })
        print("Dados do paciente foram alterados!")

def marcarConsulta():
    
    print("Marcar Consulta")
    medico = buscarMedicos()
    if not medico:
        print("Médico não encontrado.")
        return
    
    paciente = buscarPacientes()
    if not paciente:
        print("Paciente não encontrado.")
        return
    
    data = input("Data da consulta: ")
    horario = input("Horário da consulta: ")
    
    lista_consultas.append({
        'medico': medico['nome'],
        'paciente': paciente['nome'],
        'data': data,
        'horario': horario
    })
    print("Consulta agendada!")



def emitirRelatorio():
   
    print("Relatório de Consultas")
    if not lista_consultas:
        print("Não há consultas agendadas.")
        return
    
    for consulta in lista_consultas:
        print(f"Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Data: {consulta['data']}, Horário: {consulta['horario']}")



def main():
    while True:
        lang = input("1 - Cadastrar Médico\n"
                     "2 - Cadastrar Pacientes\n"
                     "3 - Cadastrar Convênios\n"
                     "4 - Buscar Médicos\n"
                     "5 - Buscar Pacientes\n"
                     "6 - Buscar Convênios\n"
                     "7 - Alterar Médicos\n"
                     "8 - Alterar Pacientes\n"
                     "9 - Marcar Consulta\n"
                     "10 - Emitir Relatório\n"
                     "11 - Marcar compromisso\n"
                     "12 - Encerrar Programa\n"
                     "O que você deseja fazer? ")

        match lang:
            case "1":
                cadastrarMedicos()
            case "2":
                cadastrarPacientes()
            case "3":
                cadastrarConvenios()
            case "4":
                buscarMedicos()
            case "5":
                buscarPacientes()
            case "6":
                buscarConvenios()
            case "7":
                alterarMedicos()
            case "8":
                alterarPacientes()
            case "9":
                marcarConsulta()
            case "10":
                emitirRelatorio()
            case "12":
                print("Programa encerrado.")
            case "11":
                marcarCompromisso()
                break
            case _:
                print("Escolha uma opção válida")

        mais = input('Deseja fazer algo mais? Digite sim ou não: ')
        if mais != 'sim':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
