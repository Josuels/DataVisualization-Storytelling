fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.yaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=8)
ax.tick_params(which='minor', length=5, labelsize=8, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite Superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite Inferior")
ax.plot(X, Y3, linewidth=0, 
        marker="D", markerfacecolor='w', markeredgecolor='0')

ax.set_title("Josué Lopes Santos", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marca Menor
circle(1, 1)
text(1, 0.8, "2101111")

#Salvar o arquivo
from google.colab import files
plt.savefig("GraficoJosueLopes.png")
files.download("GraficoJosueLopes.png")
