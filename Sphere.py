from Hittable import Hittable, HitRecord
from Vec3 import Vec3,dot
from Ray import Ray
import math

class Sphere(Hittable):
    def __init__(self,center:Vec3, radius:float) -> None:
        self.center = center
        self.radius = max(0,radius)

    def hit(self,r:Ray, ray_tmin:float, ray_tmax:float,rec:HitRecord):
        oc = self.center - r.origin
        a = r.direction.length_squared()
        h = dot(r.direction, oc)
        c = oc.length_squared() - self.radius**2
        discriminant = h**2 - a * c

        if (discriminant < 0) :
            return False
        
        sqrtd = math.sqrt(discriminant)

        root:float = (h - sqrtd)/a

        if root <= ray_tmin or ray_tmax <= root:
            root = (h + sqrtd)/a
            if root <= ray_tmin or  ray_tmax <= root :
                return False
            
        rec.t = root
        rec.point = r.at(rec.t)
        rec.normal = (rec.point - self.center)/self.radius
        outward_normal = (rec.point - self.center)/self.radius
        rec.set_face_normal(r,outward_normal)
        return True