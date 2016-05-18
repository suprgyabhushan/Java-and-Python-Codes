public class Solution
{
	public String getHint(String secret, String guess)
	{
	    //table records the appearance of a digit
	    //digit from secret will increase the counter
	    //digit from guess will decrease the counter
	    int[] count = new int[10];
	
	    int counterA = 0, counterB = 0;
	
	    for(int i = 0; i < secret.length(); i++){
	        int a = secret.charAt(i) - '0', b = guess.charAt(i) - '0';
			System.out.println(a);
			System.out.println(b);
	        if( a == b)
			{
	            //accurate match (same digit with same position)
	            counterA ++;
	        }

			else
			{
				//if prev part of guess has curr digit in secret
            	//then we found a pair that has same digit with different position
            	if(count[a] < 0) counterB ++;

            	//if prev part of secret has curr digit in guess
            	//then we found a pair that has same digit with different position                
            	if(count[b] > 0) counterB ++;

            count[a] ++;
            count[b] --;
			}
	    }
	   return counterA + "A" + counterB + "B";
}
}
