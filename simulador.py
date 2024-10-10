from stack import Stack
import json

# Leer el archivo JSON
with open('automata_pila.json', 'r') as file:
    automaton = json.load(file)

# Implementación del stack
stack = Stack()

# Inicializar el autómata
current_state = automaton["initial_state"]
stack.push(automaton["initial_stack_symbol"])

# Simulación de la entrada
input_string = "0011"  # Cadena de entrada a procesar
input_index = 0

# Función para realizar transiciones
def make_transition(state, symbol, stack_symbol):
    key = f"({state}, {symbol}, {stack_symbol})"
    if key in automaton["transitions"]:
        return automaton["transitions"][key]
    else:
        return None

# Procesar la entrada paso a paso
while input_index < len(input_string):
    current_symbol = input_string[input_index]
    top_stack = stack.peek()
    
    # Verificar si hay una transición para el estado actual, símbolo de entrada y símbolo de pila
    transition = make_transition(current_state, current_symbol, top_stack)
    
    if transition:
        # Aplicar la transición
        
        new_state, new_stack_symbols = transition
        print(f"Transición: ({current_state}, {current_symbol}, {top_stack}) -> ({new_state}, {new_stack_symbols})")
        
        # Actualizar el estado
        current_state = new_state
        
        # Actualizar la pila: Primero se hace pop del símbolo de la cima
        stack.pop()
        
        # Luego, si hay nuevos símbolos para la pila, los agregamos (en orden inverso para mantener LIFO)
        if new_stack_symbols:
            for symbol in reversed(new_stack_symbols):
                if symbol == "Z":
                    stack.push("Z0")
                elif symbol == "0":
                    continue
                else:
                    stack.push(symbol)
        
        # Avanzar en la cadena de entrada
        input_index += 1
    else:
        print(f"No hay transición definida para ({current_state}, {current_symbol}, {top_stack})")
        break

# Verificar si llegamos a un estado final
if current_state in automaton["final_states"]:
    print(f"Cadena aceptada en el estado {current_state}")
else:
    print(f"Cadena no aceptada. Estado final: {current_state}")
