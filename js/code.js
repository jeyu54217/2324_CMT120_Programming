const fs = require('fs');

function exercise1(num, den) {
    /**
     * Reduce a fraction to its lowest terms.
     *
     * @param {number} num - The numerator of the fraction.
     * @param {number} den - The denominator of the fraction.
     * @returns {Array} An array containing the reduced numerator and denominator.
     */
    function gcd(a, b) {
        // Function to find the Greatest Common Divisor (GCD)
        while (b !== 0) {
            let temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }

    // Compute GCD of numerator and denominator
    let greatestCommonDivisor = gcd(num, den);

    // Reduce the fraction
    let reducedNum = num / greatestCommonDivisor;
    let reducedDen = den / greatestCommonDivisor;

    return [reducedNum, reducedDen];
}

function exercise2(day, month, year) {
    /**
     * Check if a given date is a magic date.
     *
     * A magic date occurs when the day multiplied by the month equals the last two digits of the year.
     *
     * @param {number} day - The day of the date.
     * @param {number} month - The month of the date.
     * @param {number} year - The year of the date.
     * @returns {boolean} True if the date is a magic date, False otherwise.
     */
    // Multiply day and month
    let product = day * month;

    // Get last two digits of the year
    let lastTwoDigits = year % 100;

    // Check if product equals the last two digits of the year
    return product === lastTwoDigits;
}

function exercise3(l) {
    /**
     * Generate all possible sublists of a given array.
     *
     * @param {Array} l - The array from which sublists are to be generated.
     * @returns {Array} An array of all possible sublists.
     */
    let sublists = [[]];
    for (let i = 0; i < l.length; i++) {
        for (let j = i + 1; j <= l.length; j++) {
            // Slice the input array to get the sublist
            let sublist = l.slice(i, j);
            sublists.push(sublist);
        }
    }
    return sublists;
}
    

function exercise4(word) {

    /**
     * Translate an English word to Pig Latin.
     *
     * Rules:
     * - If the word begins with a consonant (including 'y'), move all letters before the first vowel to the end and add 'ay'.
     * - If the word begins with a vowel (excluding 'y'), add 'way' to the end.
     * - Handle uppercase letters and punctuation.
     *
     * @param {string} word - The English word to translate.
     * @returns {string} The translated Pig Latin word.
     */
    // Check if the word is empty
    if (!word) {
        return word;
    }

    // Check for punctuation at the end
    let punctuation = '';
    if ([',', '.', '?', '!'].includes(word[word.length - 1])) {
        punctuation = word[word.length - 1];
        word = word.slice(0, -1);
    }

    // Find the first vowel in the word
    let firstVowelIndex = word.toLowerCase().search(/[aeiou]/);

    // Translate to Pig Latin
    let translatedWord;
    if (firstVowelIndex === 0) {
        translatedWord = word + 'way';
    } else {
        let start = word.slice(firstVowelIndex);
        let end = word.slice(0, firstVowelIndex) + 'ay';
        translatedWord = start + end;
    }

    // Handle uppercase
    if (word[0] === word[0].toUpperCase()) {
        translatedWord = translatedWord.charAt(0).toUpperCase() + translatedWord.slice(1).toLowerCase();
    }

    return translatedWord + punctuation;
}
    


function exercise5(message) {
    /**
     * Encode a string into Morse code.
     *
     * @param {string} message - The string of letters and numbers to encode.
     * @returns {string} The Morse code representation of the input string.
     */
    // Morse code object
    const morseCode = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        '0': '-----'
    };

    // Convert to uppercase and remove non-alphanumeric characters
    message = message.toUpperCase().replace(/[^A-Z0-9]/g, '');

    // Encode the text into Morse code
    let morseCodeRepresentation = message
        .split('')
        .map(char => morseCode[char])
        .join(' ');

    return morseCodeRepresentation;
}
    

function exercise6(num) {
    /**
     * Convert an integer to its English words representation.
     *
     * @param {number} num - The integer to convert, between 0 and 999 inclusive.
     * @returns {string} The English words for the input number.
     */
    // Define objects for number segments
    const ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    const teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
                    'seventeen', 'eighteen', 'nineteen'];
    const tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
    
    // Initialize the result string
    let words = '';
    
    // Handle hundreds
    if (num >= 100) {
        if (ones[Math.floor(num / 100)] > 1) {
            words += ones[Math.floor(num / 100)] + ' hundred';
        } else if (ones[Math.floor(num / 100)] === 1) {
            words += 'one hundred';
        }
        num %= 100;
        if (num) {
            words += ' and ';
        }
    }
    
    // Handle tens and ones
    if (num >= 20) {
        words += tens[Math.floor(num / 10)];
        num %= 10;
        if (num) {
            words += '-' + ones[num];
        }
    } else if (num >= 10) {
        words += teens[num - 10];
    } else if (num > 0) {
        words += ones[num];
    }
    
    return words;
}



function exercise7(filename) {
    /**
     * Identify functions in a JavaScript source file that do not have preceding comments.
     *
     * @param {string} filename - The path to the source file to analyze.
     * @returns {Array} An array of function names without preceding comments.
     */
    const fs = require('fs');

    // Initialize an array to hold the names of functions without comments
    let functionsWithoutComments = [];

    // Read the file and split into lines
    let lines = fs.readFileSync(filename, 'utf-8').split('\n');

    // Iterate through the lines of the file
    for (let i = 0; i < lines.length; i++) {
        // Check if the line starts with 'function '
        if (lines[i].startsWith('function ')) {
            // Extract the function name
            let functionName = lines[i].split('(')[0].replace('function ', '').trim();
            // Check if the previous line is a comment
            if (i === 0 || !lines[i-1].trim().startsWith('//')) {
                functionsWithoutComments.push(functionName);
            }
        }
    }

    return functionsWithoutComments;
}


function exercise8(filename, length) {
        /**
         * Read lines from a file and split them into strings with a maximum length.
         *
         * @param {string} filename - The path to the file to read.
         * @param {number} length - The maximum allowed length for each line.
         * @returns {Array} An array of strings, each not exceeding the maximum length.
         */
        // Read the file and split into words
        const text = fs.readFileSync(filename, 'utf-8');
        const words = text.split(/\s+/);
    
        // Initialize an array to store the processed lines
        let processedLines = [];
        let currentLine = [];
        let currentLength = 0;
    
        words.forEach(word => {
            // Check if adding the next word would exceed the maxLength
            if (currentLength + word.length + currentLine.length > length) {
                // Join the current line and add it to the processed lines
                processedLines.push(currentLine.join(' '));
                currentLine = [word];
                currentLength = word.length;
            } else {
                // Add the word to the current line
                currentLine.push(word);
                currentLength += word.length;
            }
        });
    
        // Add the last line if it's not empty
        if (currentLine.length) {
            processedLines.push(currentLine.join(' '));
        }
    
        return processedLines;
    }


function exercise9(start, end, moves) {

    /**
     * Determine if a knight can reach the final position from the initial position in at most the given number of moves.
     *
     * @param {string} start - The initial position of the knight (e.g., 'a1').
     * @param {string} end - The final position to reach (e.g., 'c5').
     * @param {number} moves - The maximum number of moves allowed.
     * @returns {boolean} True if the knight can reach the final position within the given moves, False otherwise.
     */
    // Convert the position to (row, column)
    function posToRC(pos) {
        let col = pos.charCodeAt(0) - 'a'.charCodeAt(0);
        let row = parseInt(pos[1], 10) - 1;
        return [row, col];
    }

    // Calculate possible moves from a given position
    function getKnightMoves(pos) {
        let [row, col] = pos;
        let moves = [
            [row + 2, col + 1], [row + 2, col - 1],
            [row - 2, col + 1], [row - 2, col - 1],
            [row + 1, col + 2], [row + 1, col - 2],
            [row - 1, col + 2], [row - 1, col - 2]
        ];
        return moves.filter(([r, c]) => r >= 0 && r < 8 && c >= 0 && c < 8);
    }

    // Recursive function to search for the final position
    function search(pos, final, movesRemaining) {
        if (movesRemaining < 0) {
            return false;
        }
        if (pos[0] === final[0] && pos[1] === final[1]) {
            return true;
        }
        return getKnightMoves(pos).some(nextMove => search(nextMove, final, movesRemaining - 1));
    }

    let initialRC = posToRC(start);
    let finalRC = posToRC(end);
    return search(initialRC, finalRC, moves);
}

    

function exercise10(environment) {
    /**
     * Simulate the War of Species on a grid.
     *
     * @param {Array} environment - The current state of the environment as an array of strings.
     * @returns {Array} The next state of the environment as an array of strings.
     */
    function countNeighbors(x, y) {
        // Counts the number of each species around a given cell
        const counts = {'X': 0, 'O': 0, '.': 0};
        for (let dx = -1; dx <= 1; dx++) {
            for (let dy = -1; dy <= 1; dy++) {
                if (dx === 0 && dy === 0) continue;
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < environment.length && ny >= 0 && ny < environment[0].length) {
                    counts[environment[nx][ny]]++;
                }
            }
        }
        return counts;
    }
    
    function nextCellState(x, y) {
        // Determines the next state for a single cell
        const neighbors = countNeighbors(x, y);
        const cell = environment[x][y];
        const totalNeighbors = neighbors['X'] + neighbors['O'];
        
        if (cell === '.' && Math.max(neighbors['X'], neighbors['O']) >= 2) {
            return neighbors['X'] > neighbors['O'] ? 'X' : neighbors['O'] > neighbors['X'] ? 'O' : '.';
        } else if (cell !== '.' && (totalNeighbors > 6 || neighbors[cell] < 3 || neighbors[cell === 'X' ? 'O' : 'X'] > neighbors[cell])) {
            return '.';
        } else {
            return cell;
        }
    }
    
    // Create the next state of the environment
    return environment.map((row, x) => [...row].map((_, y) => nextCellState(x, y)).join(''));
}
    


module.exports = {
    // Exercise 1
    exercise1: exercise1,

    // Exercise 2
    exercise2: exercise2,

    // Exercise 3
    exercise3: exercise3,

    // Exercise 4
    exercise4: exercise4,

    // Exercise 5
    exercise5: exercise5,

    // Exercise 6
    exercise6: exercise6,

    // Exercise 7
    exercise7: exercise7,

    // Exercise 8
    exercise8: exercise8,

    // Exercise 9
    exercise9: exercise9,

    // Exercise 10
    exercise10: exercise10,
}



