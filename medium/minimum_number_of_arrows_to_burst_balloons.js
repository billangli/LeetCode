/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    let prev_needle = 0;
    let result = 0;
    
    const sorted_points = points.sort(function(a, b) {
        if (a[1] != b[1]) {
            return a[1] < b[1] ? -1 : 1;
        } else {
            return a[0] < b[0] ? -1 : 1;
        }
    });
    
    for (let i = 0; i < sorted_points.length; i++) {
        if (result == 0 || prev_needle < sorted_points[i][0]) {
            prev_needle = sorted_points[i][1];
            result += 1;
        }
    }
    
    return result;
};
