public class Cylinder1 extends Circle {

   // override the getArea() method inherited from superclass Circle
   @Override
   public double getArea() {
      return 2*Math.PI*getRadius()*height + 2*super.getArea();
   }
   // need to change the getVolume() as well
   public double getVolume() {
      return super.getArea()*height;   // use superclass' getArea()
   }
   // override the inherited toString()
   @Override
   public String toString() {
      return "Cylinder: radius = " + getRadius() + " height = " + height;   
   }
}