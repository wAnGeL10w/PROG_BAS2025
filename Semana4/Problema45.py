#Con este diccionario elegimos palabras que generan distintas respuestas
respuestas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "como estas": "Estoy bien, gracias por preguntar.",
    "que puedes hacer": "Puedo responder preguntas simples.",
    "adios": "¡Adiós! Que tengas un buen día."
}

print("Bot activado. Escribe 'adios' para salir.")

while True:
    user_input = input("\nTú: ").lower()
    
    #Si el usuario escribe la palabra, se imprime el mensaje y se cierra el programa
    if user_input == "adios":
        print("Bot:", respuestas["adios"])
        break
    
    #Si se escribe alguna palabra que no este en el diccionario, se imprime el mensaje
    print("Bot:", respuestas.get(user_input, "No entiendo tu pregunta."))

input("\nPresione ENTER para cerrar el programa ")