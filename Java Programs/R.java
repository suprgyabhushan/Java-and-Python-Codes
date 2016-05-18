public class R{
   // Private member variables
   private int length;
   private int width;
   
   // Constructor
   public R(int length, int width) {
      this.length = length;
      this.width = width;
   }
   
  /* @Override
   public String toString() {
      return "Rectangle of length=" + length + " and width=" + width + ", subclass of " + super.toString();
   }*/
   

   public double getArea() {
      return length*width;
   }

   public double getPerimeter(){
      return (2*(length+width));
   }
}
