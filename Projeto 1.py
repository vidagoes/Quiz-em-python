print("Seja muito bem-vindo ao quiz dos Games!")
answer_user = input('Quer começar?: (S/N)')

if answer_user != "S":
   quit()

score = 0

print('Começando...')
print('Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (C )Ubisoft \n (C) Activision \n (D) EA \n ')
answer_1 = input("resposta: ") 

if answer_1 == "A" or "a":
      print("Correto!")
      score = score + 1
else:
     print("Incorreto!")

print('Qual é o nome do protagonista do GTA San Anddreas? \n (A) Franklin \n (B) Carl Jonhson \n (C) Big Smoke \n (D) Rider \n ')
answer_2 = input("resposta: ") 

if answer_2 == "B" or "b":
      print("Correto!")
      score = score + 1
else:
       print("Incorreto!")
print(f"Quiz acabou... Pontuação: {score}/2")