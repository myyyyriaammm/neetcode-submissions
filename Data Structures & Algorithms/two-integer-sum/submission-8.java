class Solution {
    public int[] twoSum(int[] nums, int target){
        HashMap<Integer, Integer> d = new HashMap<>();

        for(int i = 0; i<nums.length; i++){
            int n = nums[i];
            int nbr = target - n;

            if(d.containsKey(nbr)){
                return new int[]{d.get(nbr), i};
            }

            d.put(n,i);
        }

        return new int[]{};
    }
    
}
