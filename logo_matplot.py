import matplotlib.pyplot as plt

# Definindo os pontos para desenhar um círculo
circle = plt.Circle((0.5, 0.5), 0.4, color='blue', fill=False)

# Criando a figura e o eixo
fig, ax = plt.subplots()

# Adicionando o círculo ao eixo
ax.add_artist(circle)

# Definindo limites do eixo
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Removendo os eixos
ax.axis('off')

# Exibindo o logo
plt.show()
