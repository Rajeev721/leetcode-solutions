object Solution {
    def findDuplicates(nums: Array[Int]): List[Int] = {

        val dups:List[Int] = nums.groupBy(identity).filter{case(a,b) => b.length > 1}.keys.toList
        dups
    }
}