from micropython import const

_WIDTH       = const(648)
_HEIGHT      = const(480)
_SPI_BAUD    = const(4000_000)

_RST_PIN         = const(12)
_DC_PIN          = const(8)
_CS_PIN          = const(9)
_BUSY_PIN        = const(13)

_BUSY = const(0)  # 0=busy, 1=idle