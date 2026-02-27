import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name='acumulador',
            in_sig=[np.float32],
            out_sig=[np.float32])
        self.acc = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        y[:] = np.cumsum(x) + self.acc
        self.acc = y[-1]
        return len(y)
        
