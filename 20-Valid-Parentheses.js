/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    let array = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] == ')' && array.length > 0 && array[array.length - 1] === '('){
            array.pop();
            continue;
        }
        if (s[i] == '}' && array.length > 0 && array[array.length - 1] === '{'){
            array.pop();
            continue;
        }
        if (s[i] == ']' && array.length > 0 && array[array.length - 1] === '['){
            array.pop();
            continue;
        }
        array.push(s[i]);
    }
    return array.length === 0 ? true : false;
};