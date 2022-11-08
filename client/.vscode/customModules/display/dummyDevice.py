import framebuf

class DummyDevice(framebuf.FrameBuffer):
    def __init__(self, width, height, buf_format):
        self.width = width
        self.height = height
        self._buf = bytearray(self.width * self.height // 8)
        super().__init__(self._buf, self.width, self.height, buf_format)