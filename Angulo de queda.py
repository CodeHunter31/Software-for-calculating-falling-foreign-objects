import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt 

# Função para calcular a trajetória do objeto
def calcular_trajetoria(massa, velocidade, angulo, gravidade):
    # Convertendo o ângulo para radianos
    angulo_rad = math.radians(angulo)

    # Componentes da velocidade inicial
    v_x = velocidade * math.cos(angulo_rad)
    v_y = velocidade * math.sin(angulo_rad)

    # Tempo total de voo (2 * tempo para atingir o ápice)
    tempo_voo = (2 * v_y) / gravidade

    # Alcance máximo
    alcance = v_x * tempo_voo

    # Altura máxima
    altura_max = (v_y**2) / (2 * gravidade)

    # Gerar pontos para a trajetória
    t = 0
    delta_t = 0.01  # Pequenos intervalos de tempo
    trajetoria_x = []
    trajetoria_y = []

    while t <= tempo_voo:
        x = v_x * t
        y = (v_y * t) - (0.5 * gravidade * t**2)
        trajetoria_x.append(x)
        trajetoria_y.append(y)
        t += delta_t

    return trajetoria_x, trajetoria_y, alcance, altura_max, tempo_voo

# Função para processar os dados e exibir os resultados
def processar_dados():
    try:
        massa = float(entry_massa.get())
        velocidade = float(entry_velocidade.get())
        angulo = float(entry_angulo.get())
        gravidade = float(entry_gravidade.get())

        if massa <= 0 or velocidade <= 0 or gravidade <= 0:
            raise ValueError("Os valores devem ser maiores que zero.")

        trajetoria_x, trajetoria_y, alcance, altura_max, tempo_voo = calcular_trajetoria(
            massa, velocidade, angulo, gravidade
        )

        # Exibindo os resultados em uma janela de mensagem
        resultado = (
            f"Alcance máximo: {alcance:.2f} m\n"
            f"Altura máxima: {altura_max:.2f} m\n"
            f"Tempo total de voo: {tempo_voo:.2f} s"
        )
        messagebox.showinfo("Resultados", resultado)

        # Plotando a trajetória
        plt.figure()
        plt.plot(trajetoria_x, trajetoria_y, label="Trajetória")
        plt.title("Trajetória do Objeto")
        plt.xlabel("Distância (m)")
        plt.ylabel("Altura (m)")
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Cálculo de Queda de Objeto")

# Labels e campos de entrada
tk.Label(root, text="Massa (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_massa = tk.Entry(root)
entry_massa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Velocidade inicial (m/s):").grid(row=1, column=0, padx=10, pady=5)
entry_velocidade = tk.Entry(root)
entry_velocidade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ângulo de lançamento (°):").grid(row=2, column=0, padx=10, pady=5)
entry_angulo = tk.Entry(root)
entry_angulo.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gravidade (m/s²):").grid(row=3, column=0, padx=10, pady=5)
entry_gravidade = tk.Entry(root)
entry_gravidade.grid(row=3, column=1, padx=10, pady=5)

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", command=processar_dados)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciando o loop da interface
root.mainloop()
