class Vec3:

    def __init__(self,x,y,z):
        self.x  = x
        self.y  = y
        self.z  = z

    
    def __mul__(self, scalar):
        return Vec3(self.x*scalar, self.y*scalar, self.z*scalar)
        
    def __add__(self,v):
        if not isinstance(v,Vec3):
            return Vec3(self.x + v,self.y + v,self.z + v)
        return Vec3(self.x + v.x,self.y + v.y,self.z + v.z)
    
    def __sub__(self,v):
        if not isinstance(v,Vec3):
            return Vec3(self.x - v,self.y - v,self.z - v)
        return Vec3(self.x - v.x,self.y - v.y,self.z - v.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    
    def __truediv__(self, scalar):
        return Vec3(self.x/scalar, self.y/scalar, self.z/scalar)

    def __repr__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
    
    def write(self,image):
        image.write(f'{int(self.x * 255.99)} {int(self.y * 255.99)} {int(self.z * 255.99)} ')

    def length(self):
        return self.length_squared()**0.5

    def length_squared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    def unit_vector(self):
        return self/self.length()

Color = Vec3
Point3D = Vec3

def dot(a:Vec3, b:Vec3) -> float:
    return a.x*b.x + a.y*b.y + a.z*b.z

def cross(a, b):
    return Vec3(a.y*b.z - a.z*b.y,
                -(a.x*b.z - a.z*b.x),
                a.x*b.y - a.y*b.x)