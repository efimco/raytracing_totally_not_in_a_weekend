from Ray import Ray
from Vec3 import Vec3, dot
from abc import abstractmethod


class HitRecord:
    def __init__(self, point:Vec3, normal:Vec3, t=0.0):
        self.point = point  # This should be a point3 object
        self.normal = normal  # This should be a vec3 object
        self.t = t
        self.__front_face = True

    def set_face_normal(self,ray:Ray,outward_normal:Vec3):
        self.__front_face = dot(ray.direction,outward_normal) < 0
        self.normal =  outward_normal if self.__front_face else -outward_normal
        


class Hittable:
    @abstractmethod
    def hit(self, r, ray_tmin, ray_tmax, rec: HitRecord) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
