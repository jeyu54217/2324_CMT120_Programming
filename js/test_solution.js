var expect = require('chai').expect;
var funcsToTest = require('./' + process.env.npm_config_solutionfile);

describe("exercise1()", () => {
    it("should return [4,5] when given the input (12, 15)", () => {
        expect(funcsToTest.exercise1(12, 15)).to.be.eql([4,5]);
    });
    it("should return [3,7] when given the input (3, 7)", () => {
        expect(funcsToTest.exercise1(3, 7)).to.be.eql([3,7]);
    });
});


describe("exercise2()", () => {
    it("should return true when given the input (6, 10, 1960)", () => {
        expect(funcsToTest.exercise2(6, 10, 1960)).to.be.equal(true);
    });
    it("should return false when given the input (7, 1, 2021)", () => {
        expect(funcsToTest.exercise2(7, 1, 2021)).to.be.equal(false);
    });
});

describe("exercise3()", () => {
    it("should return the correct list given the input(['a', 2, (0, 'zero')])", () => {
        expect(funcsToTest.exercise3(["a", 2, (0, "zero")])).to.have.deep.members([
            [],
            ["a"],
            [2],
            [(0, "zero")],
            ["a", 2],
            [2, (0, "zero")],
            ["a", 2, (0, "zero")],
        ]);
    });
    it("should return the correct list given the input(['a', 1])", () => {
        expect(funcsToTest.exercise3(["a", 1])).to.have.deep.members([[], ["a"], [1], ["a", 1]]);
    });
});

describe("exercise4()", () => {
    it("should return 'omputercay' when given the input 'computer' ", () => {
        expect(funcsToTest.exercise4("computer")).to.be.eql("omputercay");
    });
    it("should return 'inkthay' when given the input 'think' ", () => {
        expect(funcsToTest.exercise4("think")).to.be.eql("inkthay");
    });
});

describe("exercise5()", () => {
    it("should return '.... . .-.. .-.. --- .-- --- .-. .-.. -..' when given the input 'Hello, World!'", () => {
        expect(funcsToTest.exercise5("Hello, World!")).to.be.eql(".... . .-.. .-.. --- .-- --- .-. .-.. -..");
    });
    it("should return '- . ... - .. -. --. .---- ..--- ...-- - . ... - .. -. --.' when given the input 'Testing, 1, 2, 3, Testing!'", () => {
        expect(funcsToTest.exercise5("Testing, 1, 2, 3, Testing!")).to.be.eql("- . ... - .. -. --. .---- ..--- ...-- - . ... - .. -. --.");
    });
});

describe("exercise6()", () => {
    it("should return 'twenty-one' when given the input 21", () => {
        expect(funcsToTest.exercise6(21)).to.be.eql("twenty-one");
    });
    it("should return 'a hundred and ninety-one' when given the input 191", () => {
        expect(funcsToTest.exercise6(191)).to.be.eql("a hundred and ninety-one");
    });
});

describe("exercise7()", () => {
    it("should return ['init', 'overdrawn'] when given the input 'code1.js'", () => {
        expect(funcsToTest.exercise7('test_data/code1.js')).to.have.deep.members(['init', 'overdrawn']);
    });
    it("should return [] when given the input 'code2.js'", () => {
        expect(funcsToTest.exercise7('test_data/code2.js')).to.have.deep.members([]);
    });
});

describe("exercise8()", () => {
    it("should return the right text when given the input 'text1.txt', 50", () => {
        expect(funcsToTest.exercise8('test_data/text1.txt', 50)).to.have.deep.members(['Alice was beginning to get very tired of sitting', 'by her sister on the bank, and of having nothing', 'to do: once or twice she had peeped into the book', 'her sister was reading, but it had no pictures or', 'conversations in it,"and what is the use of a', 'book," thought Alice, "without pictures or', 'conversations?"']);
    });
    it("should return the right text when given the input 'text1.txt', 20", () => {
        expect(funcsToTest.exercise8('test_data/text1.txt', 20)).to.have.deep.members(['Alice was beginning', 'to get very tired of', 'sitting by her', 'sister on the bank,', 'and of having', 'nothing to do: once', 'or twice she had', 'peeped into the book', 'her sister was', 'reading, but it had', 'no pictures or', 'conversations in', 'it,"and what is the', 'use of a book,"', 'thought Alice,', '"without pictures or', 'conversations?"']);
    });
});

describe("exercise9()", () => {
    it("should return true when given the input ('a1', 'c5', 2)", () => {
        expect(funcsToTest.exercise9("a1", "c5", 2)).to.be.equal(true);
    });
    it("should return false when given the input ('c6', 'h1', 3)", () => {
        expect(funcsToTest.exercise9("c6", "h1", 3)).to.be.equal(false);
    });
});

describe("exercise10()", () => {
    it('should return ["XXX.....", "XXX..OOO", "XX....O."] when given the input (["XX......", "XX....O.", ".....OOO"])', () => {
        expect(funcsToTest.exercise10(["XX......", "XX....O.", ".....OOO"])).to.have.deep.members(["XXX.....", "XXX..OOO", "XX....O."]);
    }); 
    it('should return ["XXX...", "XXOOOO", "......"] when given the input (["XX....", "XX....", "OOOOOO"])', () => {
        expect(funcsToTest.exercise10(["XX....", "XX....", "OOOOOO"])).to.have.deep.members(["XXX...", "XXOOOO", "......"]);
    }); 
});
