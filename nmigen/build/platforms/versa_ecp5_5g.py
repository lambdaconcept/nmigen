# This file is Copyright (c) 2017 Serge 'q3k' Bazanski <serge@bazanski.pl>
# License: BSD

from ..generic_platform import *
from ..lattice import *


_resources = [
    Resource("clk100", 0, Pins("P3", dir="i"), extras=["IO_TYPE=LVDS"]),

    Resource("rst_n", 0, Pins("T1", dir="i"), extras=["IO_TYPE=LVCMOS33"]),

    Resource("user_led", 0, Pins("E16", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 1, Pins("D17", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 2, Pins("D18", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 3, Pins("E18", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 4, Pins("F17", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 5, Pins("F18", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 6, Pins("E17", dir="o"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_led", 7, Pins("F16", dir="o"), extras=["IO_TYPE=LVCMOS25"]),

    Resource("user_dip_btn", 0, Pins("H2",  dir="i"), extras=["IO_TYPE=LVCMOS15"]),
    Resource("user_dip_btn", 1, Pins("K3",  dir="i"), extras=["IO_TYPE=LVCMOS15"]),
    Resource("user_dip_btn", 2, Pins("G3",  dir="i"), extras=["IO_TYPE=LVCMOS15"]),
    Resource("user_dip_btn", 3, Pins("F2",  dir="i"), extras=["IO_TYPE=LVCMOS15"]),
    Resource("user_dip_btn", 4, Pins("J18", dir="i"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_dip_btn", 5, Pins("K18", dir="i"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_dip_btn", 6, Pins("K19", dir="i"), extras=["IO_TYPE=LVCMOS25"]),
    Resource("user_dip_btn", 7, Pins("K20", dir="i"), extras=["IO_TYPE=LVCMOS25"]),

    Resource("serial", 0,
        Subsignal("tx", Pins("A11", dir="o")),
        Subsignal("rx", Pins("C11", dir="i")),
        extras=["IO_TYPE=LVCMOS33"]
    ),

    Resource("eth_clocks", 0,
        Subsignal("tx", Pins("P19", dir="o")),
        Subsignal("rx", Pins("L20", dir="i")),
        extras=["IO_TYPE=LVCMOS25"]
    ),
    Resource("eth", 0,
        Subsignal("rst_n",   Pins("U17", dir="i")),
        Subsignal("mdio",    Pins("U18", dir="io")),
        Subsignal("mdc",     Pins("T18", dir="i")),
        Subsignal("rx_ctl",  Pins("U19", dir="i")),
        Subsignal("rx_data", Pins("T20 U20 T19 R18", dir="i")),
        Subsignal("tx_ctl",  Pins("R20", dir="o")),
        Subsignal("tx_data", Pins("N19 N20 P18 P20", dir="o")),
        extras=["IO_TYPE=LVCMOS25"]
    ),

    Resource("eth_clocks", 1,
        Subsignal("tx", Pins("C20", dir="o")),
        Subsignal("rx", Pins("J19", dir="i")),
        extras=["IO_TYPE=LVCMOS25"]
    ),
    Resource("eth", 1,
        Subsignal("rst_n",   Pins("F20", dir="i")),
        Subsignal("mdio",    Pins("H20", dir="io")),
        Subsignal("mdc",     Pins("G19", dir="i")),
        Subsignal("rx_ctl",  Pins("F19", dir="i")),
        Subsignal("rx_data", Pins("G18 G16 H18 H17", dir="i")),
        Subsignal("tx_ctl",  Pins("E19", dir="o")),
        Subsignal("tx_data", Pins("J17 J16 D19 D20", dir="o")),
        extras=["IO_TYPE=LVCMOS25"]
    ),

    Resource("ext_clk", 0, DiffPairs("A4 A5", dir="i"), extras=["IO_TYPE=LVDS"]),

    Resource("pcie_x1", 0,
        Subsignal("perst", Pins("A6",  dir="i"), extras=["IO_TYPE=LVCMOS33"]),
        Subsignal("clk",
            Subsignal("p", Pins("Y11", dir="i")),
            Subsignal("n", Pins("Y12", dir="i"))
        ),
        Subsignal("rx",
            Subsignal("p", Pins("Y5",  dir="i")),
            Subsignal("n", Pins("Y6",  dir="i"))
        ),
        Subsignal("tx",
            Subsignal("p", Pins("W4",  dir="o")),
            Subsignal("n", Pins("W5",  dir="o"))
        )
    )
]


_connectors = [
   Connector("X3", [
        "None",  # (no pin 0)
        "None",  #  1 GND
        "None",  #  2 N/C
        "None",  #  3 +2V5
        "B19",   #  4 EXPCON_IO29
        "B12",   #  5 EXPCON_IO30
        "B9",    #  6 EXPCON_IO31
        "E6",    #  7 EXPCON_IO32
        "D6",    #  8 EXPCON_IO33
        "E7",    #  9 EXPCON_IO34
        "D7",    # 10 EXPCON_IO35
        "B11",   # 11 EXPCON_IO36
        "B6",    # 12 EXPCON_IO37
        "E9",    # 13 EXPCON_IO38
        "D9",    # 14 EXPCON_IO39
        "B8",    # 15 EXPCON_IO40
        "C8",    # 16 EXPCON_IO41
        "D8",    # 17 EXPCON_IO42
        "E8",    # 18 EXPCON_IO43
        "C7",    # 19 EXPCON_IO44
        "C6",    # 20 EXPCON_IO45
        "None",  # 21 +5V
        "None",  # 22 GND
        "None",  # 23 +2V5
        "None",  # 24 GND
        "None",  # 25 +3V3
        "None",  # 26 GND
        "None",  # 27 +3V3
        "None",  # 28 GND
        "None",  # 29 EXPCON_OSC
        "None",  # 30 GND
        "None",  # 31 EXPCON_CLKIN
        "None",  # 32 GND
        "None",  # 33 EXPCON_CLKOUT
        "None",  # 34 GND
        "None",  # 35 +3V3
        "None",  # 36 GND
        "None",  # 37 +3V3
        "None",  # 38 GND
        "None",  # 39 +3V3
        "None",  # 40 GND
    ]),
]


class Platform(ECP5Platform):
    default_clk_name = "clk100"
    default_clk_period = 10

    def __init__(self, **kwargs):
        super().__init__("LFE5UM5G-45F-8BG381C", _resources, _connectors, **kwargs)
