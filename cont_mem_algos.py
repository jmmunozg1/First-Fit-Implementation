def first_fit(memory, req, index):
    n = len(memory)
    intentos = 0

    while intentos < n:
        i = index % n
        base, limite = memory[i]

        if req <= limite:
            nueva_base = base + req
            nuevo_limite = limite - req

            if nuevo_limite > 0:
                memory[i] = (nueva_base, nuevo_limite)
            else:
                memory.pop(i)

                if i >= len(memory):
                    i = 0                

            return memory, nueva_base, nuevo_limite, i 

        index += 1
        intentos += 1
        
    return None