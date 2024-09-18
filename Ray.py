from Vec3 import Vec3



class Ray(Vec3):
    def __init__(self, origin:Vec3, direction:Vec3):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + self.direction*t
    
    def __getitem__(self, idx):
        return Ray(self.origin[idx], self.direction[idx])

    def __setitem__(self, idx, other):
        self.origin[idx] = other.origin
        self.direction[idx] = other.direction
    
    def __len__(self):
        return self.origin.x.size