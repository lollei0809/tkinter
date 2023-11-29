def temperature_converter(Ptemp, Punit_from, Punit_to):
    Punit_from = Punit_from[0]
    Punit_to = Punit_to[0]

    if Punit_from == 'C':
        if Punit_to == 'F':
            new = Ptemp * 1.8 + 32
        elif Punit_to == 'K':
            new = Ptemp + 273.15
        elif Punit_to == 'R':
            new = Ptemp * 9 / 5 + 273.15
        else:
            new = Ptemp

    elif Punit_from == 'F':
        if Punit_to == 'C':
            new = (Ptemp - 32) / 1.8
        elif Punit_to == 'K':
            new = (Ptemp + 459.67) * 5 / 9
        elif Punit_to == 'R':
            new = Ptemp + 459.67

    elif Punit_from == 'K':
        if Punit_to == 'C':
            new = Ptemp - 273.15
        elif Punit_to == 'F':
            new = Ptemp * 9 / 5 - 459.67
        elif Punit_to == 'R':
            new = Ptemp * 9 / 5
        else:
            new = Ptemp

    elif Punit_from == 'R':
        if Punit_to == 'C':
            new = Ptemp - 491.67 * 5 / 9
        elif Punit_to == 'F':
            new = Ptemp - 459.67
        elif Punit_to == 'k':
            new = Ptemp * 5 / 9
        else:
            new = Ptemp

    else:
        new = Ptemp

    return new

