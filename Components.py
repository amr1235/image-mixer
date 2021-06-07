real = "real"
imaginary = "imaginary"
phase = "phase"
magnitude = "magnitude"
uniform_magnitude = "uniform_magnitude"
uniform_phase = "uniform_phase"
def opposite(component) : 
    if(component == real) : 
        return imaginary 
    elif component == imaginary : 
        return real
    elif component == phase : 
        return magnitude 
    elif component == magnitude : 
        return phase
    elif component == uniform_magnitude : 
        return uniform_phase
    elif component == uniform_phase :
        return uniform_magnitude