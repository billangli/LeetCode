class Solution:
    def reformatDate(self, date: str) -> str:
        tokens = date.split()
        result = tokens[2] + "-"
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                  "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        result += months[tokens[1]] + "-"
        if len(tokens[0]) == 3:
            result += "0" + tokens[0][0]
        else:
            result += tokens[0][:2]
        return result
