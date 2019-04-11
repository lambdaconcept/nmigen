# This file is Copyright (c) 2015 Yann Sionneau <yann@sionneau.net>
# This file is Copyright (c) 2015 Florent Kermarrec <florent@enjoy-digital.fr>
# This file is Copyright (c) 2018 William D. Jones <thor0505@comcast.net>
# This file is Copyright (c) 2018 Caleb Jamison <cbjamo@gmail.com>
# License: BSD

from ..generic_platform import *
from ..xilinx import *


__all__ = ["Platform"]


_resources = [
    Resource("user_led", 0, Pins("H5",  dir="o"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_led", 1, Pins("J5",  dir="o"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_led", 2, Pins("T9",  dir="o"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_led", 3, Pins("T10", dir="o"), extras=["IOSTANDARD=LVCMOS33"]),

    Resource("rgb_led", 0,
        Subsignal("r", Pins("G6", dir="o")),
        Subsignal("g", Pins("F6", dir="o")),
        Subsignal("b", Pins("E1", dir="o")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("rgb_led", 1,
        Subsignal("r", Pins("G3", dir="o")),
        Subsignal("g", Pins("J4", dir="o")),
        Subsignal("b", Pins("G4", dir="o")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("rgb_led", 2,
        Subsignal("r", Pins("J3", dir="o")),
        Subsignal("g", Pins("J2", dir="o")),
        Subsignal("b", Pins("H4", dir="o")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("rgb_led", 3,
        Subsignal("r", Pins("K1", dir="o")),
        Subsignal("g", Pins("H6", dir="o")),
        Subsignal("b", Pins("K2", dir="o")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("user_sw", 0, Pins("A8" , dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_sw", 1, Pins("C11", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_sw", 2, Pins("C10", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_sw", 3, Pins("A10", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),

    Resource("user_btn", 0, Pins("D9", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_btn", 1, Pins("C9", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_btn", 2, Pins("B9", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("user_btn", 3, Pins("B8", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),

    Resource("clk100", 0, Pins("E3", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),

    Resource("cpu_reset", 0, Pins("C2", dir="i"), extras=["IOSTANDARD=LVCMOS33"]),

    Resource("serial", 0,
        Subsignal("tx", Pins("D10", dir="o")),
        Subsignal("rx", Pins("A9",  dir="i")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("spi", 0,
        Subsignal("clk", Pins("F1")),
        Subsignal("cs_n", Pins("C1")),
        Subsignal("mosi", Pins("H1")),
        Subsignal("miso", Pins("G1")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("i2c", 0,
        Subsignal("scl", Pins("L18")),
        Subsignal("sda", Pins("M18")),
        Subsignal("scl_pup", Pins("A14")),
        Subsignal("sda_pup", Pins("A13")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("spiflash4x", 0,  # clock needs to be accessed through STARTUPE2
        Subsignal("cs_n", Pins("L13")),
        Subsignal("dq", Pins("K17 K18 L14 M14")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),
    Resource("spiflash", 0,  # clock needs to be accessed through STARTUPE2
        Subsignal("cs_n", Pins("L13")),
        Subsignal("mosi", Pins("K17")),
        Subsignal("miso", Pins("K18")),
        Subsignal("wp", Pins("L14")),
        Subsignal("hold", Pins("M14")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),

    Resource("ddram", 0,
        Subsignal("a",
            Pins("R2 M6 N4 T1 N6 R7 V6 U7 R8 V7 R6 U6 T6 T8"),
            extras=["IOSTANDARD=SSTL135"]
        ),
        Subsignal("ba", Pins("R1 P4 P2"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("ras_n", Pins("P3"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("cas_n", Pins("M4"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("we_n", Pins("P5"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("cs_n", Pins("U8"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("dm", Pins("L1 U1"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("dq",
            Pins("K5 L3 K3 L6 M3 M1 L4 M2 V4 T5 U4 V5 V1 T3 U3 R3"),
            extras=["IOSTANDARD=SSTL135", "IN_TERM=UNTUNED_SPLIT_40"]
        ),
        Subsignal("dqs", DiffPairs("N2 N1", "U2 V2"), extras=["IOSTANDARD=DIFF_SSTL135"]),
        Subsignal("clk", DiffPairs("U9 V9"), extras=["IOSTANDARD=DIFF_SSTL135"]),
        Subsignal("cke", Pins("N5"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("odt", Pins("R5"), extras=["IOSTANDARD=SSTL135"]),
        Subsignal("reset_n", Pins("K6"), extras=["IOSTANDARD=SSTL135"]),
        extras=["SLEW=FAST"],
    ),

    Resource("eth_ref_clk", 0, Pins("G18"), extras=["IOSTANDARD=LVCMOS33"]),
    Resource("eth_clocks", 0,
        Subsignal("tx", Pins("H16")),
        Subsignal("rx", Pins("F15")),
        extras=["IOSTANDARD=LVCMOS33"]
    ),
    Resource("eth", 0,
        Subsignal("rst_n", Pins("C16")),
        Subsignal("mdio", Pins("K13")),
        Subsignal("mdc", Pins("F16")),
        Subsignal("rx_dv", Pins("G16")),
        Subsignal("rx_er", Pins("C17")),
        Subsignal("rx_data", Pins("D18 E17 E18 G17")),
        Subsignal("tx_en", Pins("H15")),
        Subsignal("tx_data", Pins("H14 J14 J13 H17")),
        Subsignal("col", Pins("D17")),
        Subsignal("crs", Pins("G14")),
        extras=["IOSTANDARD=LVCMOS33"]
    )
]


_connectors = [
    Connector("pmoda", "G13 B11 A11 D12 D13 B18 A18 K16"),
    Connector("pmodb", "E15 E16 D15 C15 J17 J18 K15 J15"),
    Connector("pmodc", "U12 V12 V10 V11 U14 V14 T13 U13"),
    Connector("pmodd", "D4 D3 F4 F3 E2 D2 H2 G2"),
    Connector("ck_io", {
        # Outer Digital Header
        "ck_io0" : "V15",
        "ck_io1" : "U16",
        "ck_io2" : "P14",
        "ck_io3" : "T11",
        "ck_io4" : "R12",
        "ck_io5" : "T14",
        "ck_io6" : "T15",
        "ck_io7" : "T16",
        "ck_io8" : "N15",
        "ck_io9" : "M16",
        "ck_io10" : "V17",
        "ck_io11" : "U18",
        "ck_io12" : "R17",
        "ck_io13" : "P17",

        # Inner Digital Header
        "ck_io26" : "U11",
        "ck_io27" : "V16",
        "ck_io28" : "M13",
        "ck_io29" : "R10",
        "ck_io30" : "R11",
        "ck_io31" : "R13",
        "ck_io32" : "R15",
        "ck_io33" : "P15",
        "ck_io34" : "R16",
        "ck_io35" : "N16",
        "ck_io36" : "N14",
        "ck_io37" : "U17",
        "ck_io38" : "T18",
        "ck_io39" : "R18",
        "ck_io40" : "P18",
        "ck_io41" : "N17",

        # Outer Analog Header as Digital IO
        "ck_a0" : "F5",
        "ck_a1" : "D8",
        "ck_a2" : "C7",
        "ck_a3" : "E7",
        "ck_a4" : "D7",
        "ck_a5" : "D5",

        # Inner Analog Header as Digital IO
        "ck_io20" : "B7",
        "ck_io21" : "B6",
        "ck_io22" : "E6",
        "ck_io23" : "E5",
        "ck_io24" : "A4",
        "ck_io25" : "A3",
    }),
    Connector("XADC", {
        # Outer Analog Header
        "vaux4_n" : "C5",
        "vaux4_p" : "C6",
        "vaux5_n" : "A5",
        "vaux5_p" : "A6",
        "vaux6_n" : "B4",
        "vaux6_p" : "C4",
        "vaux7_n" : "A1",
        "vaux7_p" : "B1",
        "vaux15_n" : "B2",
        "vaux15_p" : "B3",
        "vaux0_n" : "C14",
        "vaux0_p" : "D14",

        # Inner Analog Header
        "vaux12_n" : "B7",
        "vaux12_p" : "B6",
        "vaux13_n" : "E6",
        "vaux13_p" : "E5",
        "vaux14_n" : "A4",
        "vaux14_p" : "A3",

        # Power Measurements
        "vsnsuv_n" : "B17",
        "vsnsuv_p" : "B16",
        "vsns5v0_n" : "B12",
        "vsns5v0_p" : "C12",
        "isns5v0_n" : "F14",
        "isns5v0_n" : "F13",
        "isns0v95_n" : "A16",
        "isns0v95_n" : "A15",
    })
]


class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.0

    def __init__(self, toolchain="vivado"):
        super().__init__("xc7a35ticsg324-1L", _resources, _connectors, toolchain=toolchain)
        self.add_command("set_property INTERNAL_VREF 0.675 [get_iobanks 34]")
