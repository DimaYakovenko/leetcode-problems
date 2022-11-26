class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys_to_values = {'type':[],'color':[], 'name':[]}
        for item in items:
            keys_to_values['type'].append(item[0])
            keys_to_values['color'].append(item[1])
            keys_to_values['name'].append(item[2])
        return keys_to_values[ruleKey].count(ruleValue)