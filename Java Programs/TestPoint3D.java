// A test driver program for Point3D class
public class TestPoint3D {
   public static void main(String[] args) {
      Point3D p1 = new Point3D(1, 2, 3);
      System.out.println(p1);
      System.out.println(p1.getX());  // Inherited from superclass
      System.out.println(p1.getY());  // Inherited from superclass
      System.out.println(p1.getZ());  // this class
      p1.setX(4);  // Inherited from superclass
      p1.setY(5);  // Inherited from superclass
      p1.setZ(6);  // this class
      System.out.println(p1);
   }
}