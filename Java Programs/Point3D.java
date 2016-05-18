// Define Point3D, subclass of Point
public class Point3D extends Point {
   // Private member variable
   private int z;
 
   // Constructors
   public Point3D() {  // default no-arg constructor
      super();      // Call superclass' no-arg constructor Point()
      z = 0;
   }
   public Point3D(int x, int y, int z) {
      super(x, y);  // Call superclass' Point(x, y)
      this.z = z;
   }
 
   // Public getter/setter for private variable
   public int getZ() {
      return z;
   }
   public void setZ(int z) {
      this.z = z;
   }
 
   // toString() to describe itself
   @Override
   public String toString() {
      return "(" + super.getX() + "," + super.getY() + "," + z + ")";
   }
}