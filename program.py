import movie_manager as mml

def main():
    mm = mml.new_movie_manager()

    while True:
        line = input()
        
        if line == '':    # checks if input is empty line , if so
            break         # it breaks out of while loop
        commands = line.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)
        elif commands[0] == "RA":
            commandRA(commands, mm)
        elif commands[0] == "RF":
            commandRF(commands, mm)
        elif commands[0] == "AA":
            commandAA(commands, mm)
        elif commands[0] == "AR":
            commandAR(commands, mm)

def commandRR(commands, mm):
    name = commands[1]
    if mml.has_director(mm, name):
        print("Realizador existente.")
    else:
        mml.add_director(mm, name)
        print("Realizador registado com sucesso.")
 
def commandRA(commands, mm):
    name = commands[1]
    if mml.has_actor(mm, name):
        print("Ator existente.")
    else:
        mml.add_actor(mm, name)
        print("Ator registado com sucesso.")

def commandRF(commands, mm):
    title = commands[1]
    director_name = commands[2]
    genre = commands[3]

    if not mml.has_director(mm, director_name):
        print("Realizador inexistente.")
    else:
        if mml.has_movie(mm, title, director_name, genre):
            print("Filme existente.")
        else:
            mml.add_movie(mml, title, director_name, genre)
            print("Filme adicionado com sucesso")

def commandAA(commands, mm):
    title = commands[1]
    director_name = commands[2]
    actor_name = commands[3]
    if not mml.has_director(mm, director_name):
        print("Realizador inexistente")
    else:
        if not mml.has_movie(mm, director_name, title):
            print("Filme inexistente")
        else:
            if not mml.has_actor(mm, director_name, title, actor_name):
                print("Actor inexistente")
            else:
                mml.add_actor(mm, director_name, title, actor_name)
                print("Ator adicionado com sucesso")

def commandAR(commands, mm):
    title = commands[1]
    director_name = commands[2]
    rating = commands[3]
    if not mml.has_director(mm, director_name):
        print("Realizador inexistente.")
    elif not mml.has_movie(mm, title, director_name):
        print("Filme inexistente.")
    else:
        mml.change_rating(mm, director_name, title, rating)
        print("Rating alterado com sucesso.")

if __name__ == "__main__":
    main()

 