def cross(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]

def edge_cross(a, b, p):
    ab = [b[0] - a[0], b[1] - a[1]]
    ap = [p[0] - a[0], p[1] - a[1]]

    return cross(ab, ap)

def is_in_triangle(triangle, vec):
    if edge_cross(triangle[0], triangle[1], vec) > 0:
        return False
    
    if edge_cross(triangle[1], triangle[2], vec) > 0:
        return False

    if edge_cross(triangle[2], triangle[0], vec) > 0:
        return False

    return True    

def clear(framebuffer, width, height):
    for i in range(width * height):
        framebuffer[i] = 0

def display(framebuffer, width, height):
    for y in range(height):
        row_start = y * width
        line = " ".join(str(framebuffer[row_start + x]) for x in range(width))
        print(line, end=str(y) + "\n")
        


def rasterize(triangles, framebuffer, width, height):
    for triangle in triangles:
        xmin = min(triangle[0][0], triangle[1][0], triangle[2][0])
        xmax = max(triangle[0][0], triangle[1][0], triangle[2][0])
        ymin = min(triangle[0][1], triangle[1][1], triangle[2][1])
        ymax = max(triangle[0][1], triangle[1][1], triangle[2][1])

        for y in range(ymin, ymax + 1, 1):
            for x in range(xmin, xmax + 1, 1):
                if x >= width or x < 0 or y >= height or y < 0: 
                    continue
                
                if is_in_triangle(triangle, [x, y]):
                    index = x + y * width
                    framebuffer[index] = "1"
         
def main():
    triangle = [[10,10], [12,15], [15, 10]]
    framebuffer = [0 for xy in range(25 * 25)]
    
    while True:
        clear(framebuffer, 25, 25)
        rasterize([triangle], framebuffer, 25, 25)
        display(framebuffer, 25, 25)
        x = input("continue")
        triangle[0][1] += 1
        triangle[1][1] += 1
        triangle[2][1] += 1
        

main()
