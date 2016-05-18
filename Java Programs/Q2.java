public class Q2 {


	public void printDetails(R[] rs)
	{
		for(R r : rs){
			System.out.println(r.getArea());
		}
	}
   public static void main(String[] args) {
      R r1 = new R(4, 5);
      //System.out.println(r1.getArea());
      System.out.println("Area is " + r1.getArea());
      System.out.println("Perimeter is " + r1.getPerimeter());
      
      R s1 = new Square(4);
      //System.out.println(s2);
      System.out.println("Area is " + s1.getArea());
      System.out.println("Perimeter is " + s1.getPerimeter());

       R p1 = new Point();
      //System.out.println(s2);
      System.out.println("Area is " + p1.getArea());
      System.out.println("Perimeter is " + p1.getPerimeter());

      R[] ra = {r1,s1,p1};
      printDetails(ra);

      }
}