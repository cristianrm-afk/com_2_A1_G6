import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """
    Bloque estadístico:
    - Media
    - Potencia
    - Varianza
    """

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Statistics Block",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        mean = np.mean(x)
        power = np.mean(x**2)
        variance = np.var(x)

        print("Media:", mean)
        print("Potencia:", power)
        print("Varianza:", variance)
        print("------------------")

        y[:] = x  # deja pasar la señal

        return len(y)