from pynput import mouse

def on_move(x, y):
    print(x,y)

with mouse.Listener(suppress=True, on_move=on_move) as m:
    m.join()