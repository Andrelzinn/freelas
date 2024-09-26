feitos = -1

while True:
    mensagem = input()
    
    if mensagem == 'É o fim da Estrada pra Sheldon Cooper':
        break

    if mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
        print("Não xingue seus amigos Sheldon!")
        continue
    if feitos == -1 and mensagem == 'Começou a Trabalhar na Caltech':
        feitos = 0
    elif feitos == 0 and mensagem == 'Trabalho sobre a String Theory':
        feitos = 1
    elif feitos == 1 and mensagem == 'Ganhar o Chancellor de ciência':
        feitos = 2
    elif feitos == 2 and mensagem == 'Pensar na Teoria de Cooper-Hofstader':
        feitos = 3
    elif feitos == 3 and mensagem == 'Criou a Super Assimetria':
        feitos = 4
    elif feitos == 4 and mensagem == 'Ganhar o Nobel':
        feitos = 5
        break

if feitos == -1:
    print("Que potencial desperdiçado...")
elif feitos <= 1:
    print("Tão perto, mas tão longe")
elif feitos <= 3:
    print("Não desista Sheldon, você ainda têm muito para alcançar!")
elif feitos == 4:
    print("Nãoooooo, esse momento ia ser seu Sheldon")
elif feitos == 5:
    print("Você conseguiu Sheldon, o Nobel é seu!!!")

