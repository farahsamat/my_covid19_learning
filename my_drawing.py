from src.shapes import Triangle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()

# challenge: create a rectangle - 50 width, 150 height, and yellow color
rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(200)
rect2.set_y(200)
rect2.draw()

# triangle
tri = Triangle(50, 5, 100, 5, 100, 200)
tri.draw()

# oval
oval1= Oval()
oval1.set_height(100)
oval1.set_width(250)
oval1.set_color("fuchsia")
oval1.set_x(100)
oval1.set_y(100)
oval1.draw()


#random customization
surprise_tri = Triangle()
surprise_tri.randomize()
surprise_tri.draw()

surprise_rect = Rectangle()
surprise_rect.randomize()
surprise_rect.draw()

Paper.display()