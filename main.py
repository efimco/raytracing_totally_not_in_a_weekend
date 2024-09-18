
from Vec3 import Vec3,Color,Point3D,dot
from Ray import Ray
import math
from Hittable import Hittable, HitRecord
from Sphere import Sphere

def hit_sphere(center:Vec3,radius,ray:Ray):
    oc = center - ray.origin
    a = ray.direction.length_squared()
    h = dot(ray.direction, oc)
    c = oc.length_squared() - radius**2
    discriminant = h**2 - a * c
    if (discriminant < 0) :
        return -1.0
    else: 
        return (h - math.sqrt(discriminant) ) / (a)

def ray_color(ray:Ray, world):
    rec = HitRecord(Vec3(0,0,0),Vec3(0,0,0))
    for item in world:
        if item.hit(ray,0,math.inf,rec):
            return (rec.normal + Color(1,1,1)) / 2
    #t = hit_sphere(Vec3(0,0,-1), .5, ray)

    # if t>0:
    #     N = ray.at(t).unit_vector() - Vec3(0,0,-1)
    #     return Color(N.x+1, N.y+1, N.z+1)/2
    

    unit_direction  = ray.direction.unit_vector()
    t = .5 * unit_direction.y + 1
    #print(ray.direction.unit_vector())
    return Color(1,1,1)*(1-t) + Color(0.5,.7,1)*t

def main():

    aspect_ratio = 16.0/9.0

    #image

    image_width = 400
    image_height = int(image_width/aspect_ratio) 
    image_height = image_height if image_height>=1 else 1

    #viewport

    viewport_image_height = 2
    viewport_image_width = viewport_image_height * aspect_ratio
    focal_length = 1.0


    #camera

    cam_origin  = Vec3(0,0,0)

    
    viewport_u = Vec3(viewport_image_width,0,0)
    viewport_v = Vec3(0,-viewport_image_height,0)

    pixel_delta_u = viewport_u/image_width
    pixel_delta_v = viewport_v/image_height


    viewport_upper_left_pixel = cam_origin - Vec3(0,0,focal_length) - viewport_u/2 - viewport_v /2
    pixel00 = viewport_upper_left_pixel + (pixel_delta_u + pixel_delta_v)/2

    #World
    world = list()
    world.append(Sphere(Vec3(0,0,-1),.5))
    world.append(Sphere(Vec3(0,-100.5,-1),99))
    

    with open('image.ppm','w') as image:
        image.write('P3\n')
        image.write(f'{image_width} {image_height}\n')
        image.write('255\n')
        for j in range(image_height):
            image.write('\n')
            for i in range(image_width):
                pixel = pixel00 + (pixel_delta_u*i) + (pixel_delta_v *j)
                ray_dir = pixel - cam_origin
                ray = Ray(cam_origin,ray_dir)

                pixel_color = ray_color(ray,world)

                pixel_color.write(image)


if __name__ == '__main__':
    main()