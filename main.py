import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
from matplotlib.patches import Arrow

if __name__ == '__main__':
    ampl = 2
    phase = -np.pi/2 # np.pi/3.0

    ##########################################################
    Writer = writers['ffmpeg']
    writer = Writer(fps=30, metadata=dict(artist='Tamas Csonka'), bitrate=200)

    phasor = ampl * np.exp(1j * phase)

    circx = np.linspace(-ampl, ampl, 200)
    circy = np.sqrt(ampl * ampl - circx**2)

    sinx = []
    siny = []

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 10))

    ax1.plot(circx, circy, 'k--')
    ax1.plot(circx, -circy, 'k--')
    ax1.axis('equal')
    ax1.set_xlim([-2.5, 2.5])
    ax1.set_xlabel('Re')
    ax1.set_ylabel('Im')

    ax2.set_xlim([-2.5, 2.5])
    ax2.set_ylim([360, -2])
    ax2.set_xlabel('x(t)')
    ax2.set_ylabel('t')

    line1, = ax1.plot([], [], lw=3)
    line3, = ax1.plot([], [], lw=1, color='k', ls=':')

    line2, = ax2.plot([], [], lw=2, color='r')
    line4, = ax2.plot([], [], lw=1, color='k', ls=':')

    line = [line1, line2, line3, line4]

    arrow = Arrow(0, 0, ampl * np.cos(phase), ampl * np.sin(phase), fc='g', width=0.3)
    ax1.add_patch(arrow)

    def init():
        line[0].set_data([], [])
        line[1].set_data([], [])
        line[2].set_data([], [])
        line[3].set_data([], [])

        return line

    def animate(i):
        ang = phase + i * np.pi / 45.0
        x = ampl * np.cos(ang)
        y = ampl * np.sin(ang)

        siny.append(i)
        sinx.append(ampl * np.cos(ang))

        line[0].set_data([0, x], [0, y])
        line[2].set_data([x, x], [-2.5, y])

        line[1].set_data(sinx, siny)
        line[3].set_data([x, x], [-2, i])
        return line

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=361, interval=50, repeat=False)

    plt.show()
