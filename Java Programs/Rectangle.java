// Define Rectangle, subclass of Shape
public class Rectangle extends Shape {
   // Private member variables
   private int length;
   private int width;
   
   // Constructor
   public Rectangle(String color, int length, int width) {
      super(color);
      this.length = length;
      this.width = width;
   }
   
   @Override
   public String toString() {
      return "Rectangle of length=" + length + " and width=" + width + ", subclass of " + super.toString();
   }
   
   @Override
   public double getArea() {
      return length*width;
   }
}