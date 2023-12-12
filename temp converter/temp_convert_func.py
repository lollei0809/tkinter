def temperature_converter(Ptemp, Punit_from, Punit_to):

    if isinstance(Ptemp, int) or isinstance(Ptemp, float):
        Ptemp = float(Ptemp)
    else:
        return "ERROR: temp must be a number"

    Punit_from = Punit_from[0]
    Punit_to = Punit_to[0]

    if Punit_from == 'C':
        if Ptemp < -273.15 :
            return "ERROR: temp can't be less than -273.15°C (Absolute zero)"
        if Punit_to == 'F':
            new = Ptemp * 1.8 + 32
        elif Punit_to == 'K':
            new = Ptemp + 273.15
        elif Punit_to == 'R':
            new = Ptemp * 9/5 + 491.67
        else:
            new = Ptemp

    elif Punit_from == 'F':
        if Ptemp <-459.67 :
            return "ERROR: temp can't be less than −459.67°F (Absolute zero)"
        if Punit_to == 'C':
            new = (Ptemp - 32) / 1.8
        elif Punit_to == 'K':
            new = (Ptemp + 459.67) * 5 / 9
        elif Punit_to == 'R':
            new = Ptemp + 459.67

    elif Punit_from == 'K':
        if Ptemp<0:
            return "ERROR: temp can't be less than 0K (Absolute zero)"
        if Punit_to == 'C':
            new = Ptemp - 273.15
        elif Punit_to == 'F':
            new = Ptemp * 9 / 5 - 459.67
        elif Punit_to == 'R':
            new = Ptemp * 9 / 5
        else:
            new = Ptemp

    elif Punit_from == 'R':
        if Ptemp<0:
            return "ERROR: temp can't be less than 0°R (Absolute zero)"
        if Punit_to == 'C':
            new = (Ptemp - 491.67) * 5 / 9
        elif Punit_to == 'F':
            new = Ptemp - 459.67
        elif Punit_to == 'k':
            new = Ptemp * 5 / 9
        else:
            new = Ptemp

    else:
        new = Ptemp
    new = round(new, 2)
    return new

