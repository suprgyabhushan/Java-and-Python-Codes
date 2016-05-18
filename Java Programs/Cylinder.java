// Define Cylinder class, which is a subclass of Circle
public class Cylinder extends Circle {
   private double height;   // Private member variable
   
   public Cylinder() {      // constructor 1
      super();              // invoke superclass' constructor Circle()
      height = 1.0;
   }
   public Cylinder(double radius, double height) {  // Constructor 2
      super(radius);        // invoke superclass' constructor Circle(radius)
      this.height = height;
   }
   
   public double getHeight() {
      return height;
   }
   public void setHeight(double height) {
      this.height = height;
   }
   public double getVolume() {
      return getArea()*height;   // Use Circle's getArea()
   }
}