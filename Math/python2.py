def my_animation(Y):
# Generating figure for plotting
    fig, ax = pl.subplots()
# Setting my data points
    dots, = pl.plot([], [], 'ro',)
# Plot configuration (title, grid, x, and y limits)
    pl.title("Two Masses Planetary Motion")
    ax.grid()
    ax.set_xlim(-10, 20)
    ax.set_ylim(-10, 10)

# Setting up my update frame function
    def update_frame(i):
        dots.set_data([ Y[i][0,0], Y[i][1,0] ], [ Y[i][0, 1], Y[i][1, 1] ])
        return dots,
# Defining how my animation is function (1ms intervals and n frames)
    anim = animation.FuncAnimation(fig, update_frame,  interval=1,
                        frames=n, blit=True, save_count=100)
    pl.show()