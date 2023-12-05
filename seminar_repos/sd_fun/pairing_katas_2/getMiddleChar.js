/*
  The function getMiddleChar should return the middle character of a string. If the string is of even length, return the middle two characters.
  E.g.
  'hello world!!' should return 'ow'
*/

function getMiddleChar(str) {
	if (str.length < 3) {
		return str;
	}
	const midIndex = Math.floor(str.length / 2);

	return str.charAt(midIndex);
}

module.exports = getMiddleChar;
