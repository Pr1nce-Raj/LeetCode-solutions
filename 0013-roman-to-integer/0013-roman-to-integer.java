class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> meaning = new HashMap<>();
        meaning.put('I',1);
        meaning.put('V',5);
        meaning.put('X',10);
        meaning.put('L',50);
        meaning.put('C',100);
        meaning.put('D',500);
        meaning.put('M',1000);
        int sum=0;
        int previous=0;
        int current=0;
        for (int i=s.length()-1;i>=0;i--){
            current = meaning.get(s.charAt(i));
            if (current < previous){
                sum-=current;
            }else{
                sum+=current;
            }
            previous=current;
        }
        return sum;
    }
}