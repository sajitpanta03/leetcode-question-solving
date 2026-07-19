class Solution {

    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        $groups = [];

        foreach ($strs as $str) {
            $chars = str_split($str);
            sort($chars);
            $key = implode('', $chars);

            if (!isset($groups[$key])) {
                $groups[$key] = [];
            }

            $groups[$key][] = $str;
        }

        return array_values($groups);
    }
}