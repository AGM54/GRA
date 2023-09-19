def dot(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

def subtract(v1, v2):
    return [a-b for a, b in zip(v1, v2)]

def add(v1, v2):
    return [a+b for a, b in zip(v1, v2)]

def multiply(v, scalar):
    return [i * scalar for i in v]

def magnitude(v):
    return (sum(i**2 for i in v))**0.5

def normalize(v):
    mag = magnitude(v)
    return [i/mag for i in v]

def reflectVector(normal, direction):
    reflect = multiply(normal, 2 * dot(normal, direction))
    reflect = subtract(reflect, direction)
    reflect = normalize(reflect)
    return reflect

class Light(object):
    def __init__(self, intensity=1, color=(1,1,1), lightType='None'):
        self.intensity = intensity
        self.color = color
        self.lightType = lightType

    def getLightColor(self):
        return [self.color[i] * self.intensity for i in range(3)]

    def getDiffuseColor(self, intercept):
        return None
    
    def getSpecularColor(self, intercept, viewPos):
        return None

class AmbientLight(Light):
    def __init__(self, intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "Ambient")

class DirectionalLight(Light):
    def __init__(self, direction=(0, -1, 0), intensity=1, color=(1, 1, 1)):
        self.direction = normalize(direction)
        super().__init__(intensity, color, "Directional")

    def getDiffuseColor(self, intercept):
        dir = multiply(self.direction, -1)
        intensity = max(0, min(1, dot(intercept.normal, dir) * self.intensity))
        return [color * intensity for color in self.color]
    
    def getSpecularColor(self, intercept, viewPos):
        dir = multiply(self.direction, -1)
        reflect = reflectVector(intercept.normal, dir)
        viewDir = subtract(viewPos, intercept.point)
        viewDir = normalize(viewDir)
        specIntensity = max(0, dot(viewDir, reflect)) ** intercept.obj.material.spec
        specIntensity *= self.intensity
        return [color * specIntensity for color in self.color]
