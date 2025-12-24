# PROJETO SIMPLES DO JOGO DETETIVE - Sérgio Lima | Discord: ssergiop

import os
import time
import random

#LISTAS
suspeitos = ['Kauê Santos' , 'Luan Matias', 'Alessandro']
armas = ['Caneta BIC' , 'Tesoura sem ponta' , 'Garrafinha de Alessandro']
comodos = ['Cantina' , 'Sala de aula' , 'Saída']
pistas = []

os.system('cls')
print('\n\n\n\n      O MISTÉRIO DA ESCOLA PY-THON\n      ============================\n')
comecar = str(input('\n\nPressione Enter para começar a partida: '))

time.sleep(3.0)

jogo_ativo = 'true'
while jogo_ativo != 'false':
    #RESPOSTA SECRETA
    quem = random.choice(suspeitos)
    comooque = random.choice(armas)
    onde = random.choice(comodos)
    
    round1 = 'true'
    while round1 != 'false':
        #RESPOSTAS DOS SUSPEITOS ========================

        #LUAN - INOCENTE - Onde estava
        ale_i1 = 'Tava sentado na cantina'
        ale_i2 = 'Tava procurando minha garrafa pela escola'
        ale_i3 = 'Esperando kauê terminar de copiar'
        aleifinal1 = random.choice([ale_i1 , ale_i2 , ale_i3])
        aleifinal11 = aleifinal1
        #LUAN - INOCENTE - Viu a vitima Antes do crime?
        ale_i4 = 'Sim ué'
        ale_i5 = 'Ele faltou hoje não sei como ocorreu esse crime...'
        ale_i6 = 'Ele tava saindo da escola'
        aleifinal2 = random.choice([ale_i4 , ale_i5 , ale_i6])
        aleifinal22 = aleifinal2
        #KAUÊ - INOCENTE - Alguém teria motivo para este crime?
        ale_i7 = 'Sei não em'
        ale_i8 = 'Talvez... Eu prefiro não responder...'
        ale_i9 = 'Luan não recebeu os dez pontos dele'
        ale_i10 = 'Não faço ideia'
        ale_i11 = 'Kauê tava conversando na sala e o professor deu bronca nele'
        aleifinal3 = random.choice([ale_i7 , ale_i8 , ale_i9 , ale_i10 , ale_i11])
        aleifinal33 = aleifinal3

        #Alessandro - CULPADO - Onde estava
        ale_c1 = 'Eu tava dando uma olhada na sala procurando minha garrafa.'
        ale_c2 = 'tava esperando eles na saída'
        ale_c3 = 'tava na diretoria porque eu tava rindo muito na aula'
        ale_cfinal1 = random.choice([ale_c1 , ale_c2 , ale_c3])
        alecfinal11 = ale_cfinal1
        #Alessandro - CULPADO - Viu a vitima Antes do crime?
        ale_c4 = 'Eu vi, Ele veio pra terceira aula.'
        ale_c5 = 'Ele faltou hoje'
        ale_c6 = 'Vi mas foi na saída'
        alecfinal2 = random.choice([ale_c4 , ale_c5 , ale_c6])
        alecfinal22 = alecfinal2
        #Alessandro - CULPADO - Alguém tinha motivo para o crime?
        ale_c7 = 'hm com certeza é xedow.'
        ale_c8 = 'Talvez... Eu prefiro não responder...'
        ale_c9 = 'Não faço Ideia'
        ale_c10 = 'Pode até ser kauê mas eu acho que é xedow'
        alecfinal3 = random.choice([ale_c7 , ale_c8 , ale_c9 , ale_c10])
        alecfinal33 = alecfinal3


        #LUAN - INOCENTE - Onde estava
        luan_i1 = 'Tava sentado, esperando kauê terminar de copiar'
        luan_i2 = 'Fui buscar minha bolsa, que deixei na cantina, kauê tava lá enchendo a garrafa'
        luan_i3 = 'Eu tava esperando, na saída'
        luanifinal1 = random.choice([luan_i1 , luan_i2 , luan_i3])
        luanifinal11 = luanifinal1
        #LUAN - INOCENTE - Viu a vitima Antes do crime?
        luan_i4 = 'Sim, ele deu aula hoje'
        luan_i5 = 'Não vi, tavam dizendo que ele faltou'
        luan_i6 = 'Eu vi ele no corredor indo em direção da saída'
        luanifinal2 = random.choice([luan_i4 , luan_i5 , luan_i6])
        luanifinal22 = luanifinal2
        #KAUÊ - INOCENTE - Alguém teria motivo para este crime?
        luan_i7 = 'Sei não'
        luan_i8 = 'Talvez... Eu prefiro não responder...'
        luan_i9 = 'O Professor disse que kauê era burro e mostrou a chave que kauê tava procurando'
        luan_i10 = 'Não faço ideia'
        luan_i11 = 'Alessandro tava rindo muito hoje cedo'
        luanifinal3 = random.choice([luan_i7 , luan_i8 , luan_i9 , luan_i10 , luan_i11])
        luanifinal33 = luanifinal3

        #LUAN - CULPADO - Onde estava
        luan_c1 = 'Eu... tava no, Banheiro, me limpando porquê a minha caneta estourou.'
        luan_c2 = 'Fui esperar eles, Na cantina.'
        luan_c3 = 'Tava na saída... Sozinho, esperando meus amigos'
        luan_cfinal1 = random.choice([luan_c1 , luan_c2 , luan_c3])
        luancfinal11 = luan_cfinal1
        #LUAN - CULPADO - Viu a vitima Antes do crime?
        luan_c4 = 'Eu não, acho que ele não veio.'
        luan_c5 = 'Me disseram que ele faltou.. sabe.'
        luan_c6 = 'Acho que eu vi só uma vez.. quando cheguei hoje'
        luancfinal2 = random.choice([luan_c4 , luan_c5 , luan_c6])
        luancfinal22 = luancfinal2
        #LUAN - CULPADO - Alguém tinha motivo para o crime?
        luan_c7 = 'Kauê eu acho mano.'
        luan_c8 = 'Talvez... Eu prefiro não responder...'
        luan_c9 = 'Não faço Ideia'
        luan_c10 = 'Talvez tenha sido Alessandro viu'
        luancfinal3 = random.choice([luan_c7 , luan_c8 , luan_c9 , luan_c10])
        luancfinal33 = luancfinal3


        #KAUÊ - INOCENTE - Onde estava
        kaue_i1 = 'Eu tava na sala terminando de copiar a matéria ué'
        kaue_i2 = 'Tava enchendo minha garrafa perto da saida, luan foi pra cantina'
        kaue_i3 = 'Eu tinha ido procurar o resto do pessoal na sala de aula'
        kaue_ifinal1 = random.choice([kaue_i1 , kaue_i2 , kaue_i3])
        kaue_ifinal11 = kaue_ifinal1
        #KAUÊ - INOCENTE - Viu a vitima Antes do crime?
        kaue_i4 = 'Ele deu aula hoje, no segundo horário'
        kaue_i5 = 'Ele faltou hoje... nóis teve horário vago'
        kaue_i6 = 'Vi ele indo embora pouco antes do crime'
        kaueifinal2 = random.choice([kaue_i4 , kaue_i5 , kaue_i6])
        kaueifinal22 = kaueifinal2
        #KAUÊ - INOCENTE - Alguém teria motivo para este crime?
        kaue_i7 = 'Bom... Luan tinha ficado bravo por não ter conseguido os dez pontos...'
        kaue_i8 = 'Talvez... Eu prefiro não responder...'
        kaue_i9 = 'Luan não queria fazer atividade... ai o professor deu uma prova surpresa pra ele...'
        kaue_i10 = 'Não faço ideia'
        kaue_i11 = 'Olha Alessandro não parou de rir e o professor mandou ele sair de sala..'
        kaueifinal3 = random.choice([kaue_i7 , kaue_i8 , kaue_i9 , kaue_i10 , kaue_i11])
        kauei_final33 = kaueifinal3

        #KAUÊ - CULPADO - Onde estava
        kaue_c1 = 'Eu tava na sala, Sozinho, Terminando de copiar.'
        kaue_c2 = 'Eu Tava lá Enchendo a garrafa perto da Saída.'
        kaue_c3 = 'Eu tinha ido procurar o resto do pessoal Na sala de aula tinha ninguém lá.'
        kaue_cfinal1 = random.choice([kaue_c1 , kaue_c2 , kaue_c3])
        kaue_cfinal11 = kaue_cfinal1
        #KAUÊ - CULPADO - Viu a vitima Antes do crime?
        kaue_c4 = 'Não vi ele'
        kaue_c5 = 'Não sei se ele faltou... mas acho que sim porque não vi ele hoje'
        kaue_c6 = 'Dizem, que ele tava doente'
        kauecfinal2 = random.choice([kaue_c4 , kaue_c5 , kaue_c6])
        kauecfinal22 = kauecfinal2
        #KAUÊ - CULPADO - Alguém teria motivo para este crime?
        kaue_c7 = 'Luan eu acho.'
        kaue_c8 = 'Talvez... Eu prefiro não responder...'
        kaue_c9 = 'Não faço Ideia'
        kaue_c10 = 'Alessandro parecia ansioso'
        kauecfinal3 = random.choice([kaue_c7 , kaue_c8 , kaue_c9 , kaue_c10])
        kaue_cfinal33 = kauecfinal3
        #================================================

        #SALA DE INTERROGATÓRIO =========================
        interrogatorio = 'true'
        while interrogatorio != 'false':
            os.system('cls')
            print('\n=== SALA DE INTERROGATÓRIO ===\n')
            print('[1] Interrogar\n[2] Escolher o Assassino')
            time.sleep(2.0)
            escolher1 = int(input('\nEscolha: '))
            if escolher1 == 1:
                interrogarsuspeitos = 'true'
                while interrogarsuspeitos != 'false':
                    os.system('cls')
                    print('\n=== SALA DE INTERROGATÓRIO ===\n\nSUSPEITOS:')
                    print('\n[1] Kauê\n[2] Luan\n[3] Alessandro\n\n(6) Voltar')
                    time.sleep(2.0)
                    escolher2 = int(input('\nEscolha: '))
                    
                    #INTERROGANDO - KAUÊ ============================ TERIMINADO
                    if escolher2 == 1:
                        interrogandokaue = 'true'
                        while interrogandokaue != 'false':

                            #Perguntas kauê
                            os.system('cls')
                            print('\n=== INTERROGANDO - KAUÊ ===\n')
                            print('Perguntas:\n\n[1] Onde você estava na hora do crime?\n[2] Viu a vitima antes do crime? Onde?\n[3] Alguém teria motivos para cometer este crime?\n\n(6) Voltar')
                            time.sleep(2.0)

                            #P1: Onde você estava? ------------- FUNCIONANDO
                            p1 = int(input('\nEscolha: '))
                            if p1 == 1 and quem != 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(kaue_ifinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 1 and quem == 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(kaue_cfinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))  
                            elif p1 == 6:
                                interrogandokaue = 'false'  
                            #-----------------------------------

                            #P2: Viu a vitima antes do crime? -- FUNCIONANDO
                            elif p1 == 2 and quem != 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(kaueifinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 2 and quem == 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(kauecfinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------

                            #P3: Alguém teria motivos? --------- FUNCIONANDO
                            elif p1 == 3 and quem != 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(kauei_final33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 3 and quem == 'Kauê Santos':
                                os.system('cls')
                                print('\n=== INTERROGANDO - KAUÊ ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(kaue_cfinal33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------


                    #INTERROGANDO - LUAN ============================ TERMINADO
                    elif escolher2 == 2:
                        interrogandoluan = 'true'
                        while interrogandoluan != 'false':

                            #Perguntas luan
                            os.system('cls')
                            print('\n=== INTERROGANDO - LUAN ===\n')
                            print('Perguntas:\n\n[1] Onde você estava na hora do crime?\n[2] Viu a vitima antes do crime? Onde?\n[3] Alguém teria motivos para cometer este crime?\n\n(6) Voltar')
                            time.sleep(2.0)

                            #P1: Onde você estava? ------------- FUNCIONANDO
                            p1 = int(input('\nEscolha: '))
                            if p1 == 1 and quem != 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(luanifinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 1 and quem == 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(luancfinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))  
                            elif p1 == 6:
                                interrogandoluan = 'false'  
                            #-----------------------------------

                            #P2: Viu a vitima antes do crime? -- FUNCIONANDO
                            elif p1 == 2 and quem != 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(luanifinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 2 and quem == 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(luancfinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------

                            #P3: Alguém teria motivos? --------- FUNCIONANDO
                            elif p1 == 3 and quem != 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(luanifinal33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 3 and quem == 'Luan Matias':
                                os.system('cls')
                                print('\n=== INTERROGANDO - LUAN ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(luancfinal33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------

                    #INTERROGANDO - Alessandro ============================ Fazendo
                    elif escolher2 == 3:
                        interrogandoale = 'true'
                        while interrogandoale != 'false':

                            #Perguntas alessandro
                            os.system('cls')
                            print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                            print('Perguntas:\n\n[1] Onde você estava na hora do crime?\n[2] Viu a vitima antes do crime? Onde?\n[3] Alguém teria motivos para cometer este crime?\n\n(6) Voltar')
                            time.sleep(2.0)

                            #P1: Onde você estava? ------------- FUNCIONANDO
                            p1 = int(input('\nEscolha: '))
                            if p1 == 1 and quem != 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(aleifinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 1 and quem == 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Onde você estava na hora do crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(alecfinal11))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))  
                            elif p1 == 6:
                                interrogandoale = 'false'  
                            #-----------------------------------

                            #P2: Viu a vitima antes do crime? -- FUNCIONANDO
                            elif p1 == 2 and quem != 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(aleifinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 2 and quem == 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Viu a vitima antes do crime? Onde?')
                                time.sleep(2.0)
                                print('R: {}'.format(alecfinal22))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------

                            #P3: Alguém teria motivos? --------- FUNCIONANDO
                            elif p1 == 3 and quem != 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(aleifinal33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            elif p1 == 3 and quem == 'Alessandro':
                                os.system('cls')
                                print('\n=== INTERROGANDO - ALESSANDRO ===\n')
                                print('P: Alguém teria motivos para cometer este crime?')
                                time.sleep(2.0)
                                print('R: {}'.format(alecfinal33))
                                time.sleep(2.0)
                                voltar1 = str(input('\nPressione Enter para voltar...'))
                            #-----------------------------------

                    elif escolher2 == 6:
                        interrogarsuspeitos = 'false'       
                    #================================================

            #JULGAMENTO =============================================
            elif escolher1 == 2:
                julgamento = 'true'
                while julgamento != 'false':
                    os.system('cls')
                    print('\n=== SALA DE JULGAMENTO ===\n')
                    print('Quem Você irá julgar:\n[1] Kauê\n[2] Luan\n[3] ALessandro\n')
                    julgar = int(input('Escolha: '))

                    if julgar == 1 and quem == 'Kauê Santos':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Kauê')
                        time.sleep(2.0)
                        print('\nKauê era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      O ASSASSINO\n      ===========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ VENCEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)
                    
                    elif julgar == 2 and quem == 'Luan Matias':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Luan')
                        time.sleep(2.0)
                        print('\nLuan era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      O ASSASSINO\n      ===========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ VENCEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)
                        
                    elif julgar == 3 and quem == 'Alessandro':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Alessandro')
                        time.sleep(2.0)
                        print('\nAlessandro era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      O ASSASSINO\n      ===========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ VENCEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)

                    elif julgar == 1 and quem != 'Kauê Santos':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Kauê')
                        time.sleep(2.0)
                        print('\nKauê era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      INOCENTE\n      ========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ PERDEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)

                    elif julgar == 2 and quem != 'Luan Matias':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Luan')
                        time.sleep(2.0)
                        print('\nLuan era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      INOCENTE\n      ========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ PERDEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)
        
                    elif julgar == 3 and quem != 'Alessandro':
                        os.system('cls')
                        print('\n=== SALA DE JULGAMENTO ===\n')
                        print('Você julgou Alessandro')
                        time.sleep(2.0)
                        print('\nAlessandro era...')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      INOCENTE\n      ========')
                        time.sleep(2.0)
                        os.system('cls')
                        print('\n\n\n\n      VOCÊ PERDEU O CASO\n      ==================')
                        time.sleep(1.5)
                        os.system('cls')
                        print('\nESTATÍSTICAS DA PARTIDA===============\n')
                        print('-Assassino: {}\n-Com o quê: {}\n-Onde: {}'.format(quem , comooque , onde))
                        time.sleep(40000)