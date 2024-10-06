#! /usr/bin/env python3

class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input(f"Enter Pin A input for gate {self.getLabel()}-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input(f"Enter Pin B input for gate {self.getLabel()}-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input(f"Enter Pin input for gate {self.getLabel()}-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS on this gate")



class AndGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):

    def __init__(self, label):
        AndGate.__init__(self, label)

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NorGate(OrGate):

    def __init__(self, label):
        OrGate.__init__(self, label)

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def main():
    #g1 = AndGate("G1")
    #g2 = AndGate("G2")
    #g3 = OrGate("G3")
    #g4 = NotGate("G4")
    #c1 = Connector(g1, g3)
    #c2 = Connector(g2, g3)
    #c3 = Connector(g3, g4)
    #print(g4.getOutput())

    #g5 = NandGate("G5")
    #print(g5.getOutput())

    #g6 = NorGate("G6")
    #print(g6.getOutput())

    # Создайте ряд из вентилей, который доказывал бы, что
    # NOT (( A and B) or (C and D)) это то же самое, что и
    # NOT( A and B ) and NOT (C and D).
    # Убедитесь, что используете в этой симуляции некоторые из вновь созданных
    # вами вентилей.

    g1 = AndGate("A&B")
    g2 = AndGate("C&D")

    g3 = OrGate("(A&B)||(C&D)")
    g4 = NotGate("!((A&B)||(C&D))")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    g5 = NotGate("!(A&B)")
    g6 = NotGate("!(C&D)")
    g7 = AndGate("!(A&B)&!(C&D)")

    c4 = Connector(g1, g5)
    c5 = Connector(g2, g6)
    c6 = Connector(g5, g7)
    c6 = Connector(g6, g7)

    print(g4.getOutput() == g7.getOutput())

main()
