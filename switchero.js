//  Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
//  Example:
//  'acb' --> 'bca'
//  'aabacbaa' --> 'bbabcabb'

function switchero(s) {
  let new_string = '';
  for (i = 0; i < s.length; i++) {
    if (s[i] === 'a') {
      new_string += 'b';
    } else if (s[i] === 'b') {
      new_string += 'a';
    } else {
      new_string += s[i];
    }
  }
  return new_string;
}

console.log(switchero('acb')); // -> 'bca'
console.log(switchero('aabacbaa')); // -> 'bbabcabb'
