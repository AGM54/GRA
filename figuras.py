def subtract(v1, v2):
    return [a-b for a, b in zip(v1, v2)]

def add(v1, v2):
    return [a+b for a, b in zip(v1, v2)]

def dot(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

def magnitude(v):
    return (sum(i**2 for i in v))**0.5

def normalize(v):
    mag = magnitude(v)
    return [i/mag for i in v]

def multiply(v, scalar):
    return [i * scalar for i in v]

class Intercept(object):
    def __init__(self, distance, point, normal, obj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.obj = obj

class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def ray_intersect(self, orig, dir):
        return None

class Sphere(Shape):
    def __init__(self, position, radius, material):
        self.radius = radius
        super().__init__(position, material)

    def ray_intersect(self, orig, dir):
        L = subtract(self.position, orig)
        lengthL = magnitude(L)
        tca = dot(L, dir)

        d = (lengthL ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None
        
        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        P = add(orig, multiply(dir, t0))
        normal = subtract(P, self.position)
        normal = normalize(normal)

        return Intercept(distance=t0, point=P, normal=normal, obj=self)
