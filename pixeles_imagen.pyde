tamanio_celda = 2

def setup():
    global img, columnas, filas, tamanio_celda
    size(800,450,P3D)
    img = loadImage("perro.jpg")
    columnas = width / tamanio_celda
    filas = height / tamanio_celda
    
    
def draw():
    background(0)
    loadPixels()
    
    for i in xrange(columnas):
        for j in range(filas):
            x = i*tamanio_celda + tamanio_celda / 2
            y = j*tamanio_celda + tamanio_celda / 2
            ubicacion = x + y * width
            c = img.pixels[ubicacion]
            z = ((width/4)/(float(width))*brightness(img.pixels[ubicacion])) - 100
            pushMatrix()
            translate(x,y,z)
            fill(c)
            noStroke()
            rectMode(CENTER)
            rect(0,0,tamanio_celda,tamanio_celda)
            popMatrix()     
