from .. import *


__all__ = ["CRG", "TSTriple", "Tristate"]


class CRG:
    def __init__(self, clk, rst=Const(0), reset_delay=1):
        self.clk = clk
        self.rst = rst
        self.reset_timer = Signal(max=max(2, reset_delay+1), reset=reset_delay)

    def elaborate(self, platform):
        m = Module()

        cd_por  = m.domains.cd_por  = ClockDomain(reset_less=True)
        cd_sync = m.domains.cd_sync = ClockDomain()

        m.d.comb += [
            cd_por.clk.eq(self.clk),
            cd_sync.clk.eq(self.clk),
            cd_sync.rst.eq(self.reset_timer != 0)
        ]

        with m.If(self.rst):
            m.d.por += self.reset_timer.eq(self.reset_timer.reset)
        with m.Elif(self.reset_timer != 0):
            m.d.por += self.reset_timer.eq(self.reset_timer - 1)

        return m


class TSTriple:
    def __init__(self, shape=None, min=None, max=None, reset_o=0, reset_oe=0, reset_i=0,
                 name=None):
        self.o  = Signal(shape, min=min, max=max, reset=reset_o,
                         name=None if name is None else name + "_o")
        self.oe = Signal(reset=reset_oe,
                         name=None if name is None else name + "_oe")
        self.i  = Signal(shape, min=min, max=max, reset=reset_i,
                         name=None if name is None else name + "_i")

    def __len__(self):
        return len(self.o)

    def elaborate(self, platform):
        return Fragment()

    def get_tristate(self, io):
        return Tristate(self, io)


class Tristate:
    def __init__(self, triple, io):
        self.triple = triple
        self.io     = io

    def elaborate(self, platform):
        if hasattr(platform, "get_tristate"):
            return platform.get_tristate(self.triple, self.io)

        m = Module()
        m.d.comb += self.triple.i.eq(self.io)
        m.submodules += Instance("$tribuf",
            p_WIDTH=len(self.io),
            i_EN=self.triple.oe,
            i_A=self.triple.o,
            o_Y=self.io,
        )

        f = m.elaborate(platform)
        f.flatten = True
        return f
