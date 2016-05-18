public class q2
{
    class Student
    {
        private String name;
        private int rollNumber;
        static int r = 2;
        Student(String n)
        {
            this.name = n;
            this.rollNumber = r++;
        }
        public void getname()
        {
            System.out.println(this.name);
        }
        public void setname(String value)
        {
            this.name = value;
        }
        public void getrollNumber()
        {
            System.out.println(this.rollNumber);
        }
        public void setrollNumber(int value)
        {
            this.rollNumber= value;
        }  
    }
}


