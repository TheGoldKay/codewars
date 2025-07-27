// https://www.codewars.com/kata/58b972cae826b960a300003e/train/javascript

function missingWord(nums, str) {
  let name = "";
  nums.sort((a, b) => a - b);
  str = str.replace(/ /g, '').toLowerCase();
  for (const i of nums){
    if (i >= str.length){
      return "No mission today";
    }
    name += str[i];
  }
  return name;
}
