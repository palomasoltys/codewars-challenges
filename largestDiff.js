// Find the largest difference between integers in a sorted list
// [1, 5, 6, 7, 11] => 4
// [-11, -5, 0, 5, 11] => 6
// [-11, -5, 0] => 6

function largestDiffNumber(arr) {
  let largest = 0;
  for (i = 0; i < arr.length - 1; i++) {
    const diff = arr[i + 1] - arr[i];
    if (diff > largest) {
      largest = diff;
    }
  }
  return largest;
}
console.log(largestDiffNumber([1, 5, 6, 7, 11])); // -> 4
console.log(largestDiffNumber([-11, -5, 0, 5, 11])); // -> 6
console.log(largestDiffNumber([-11, -5, 0])); // -> 6
