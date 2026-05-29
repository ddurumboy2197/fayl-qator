**Python (pytest)**
```python
import pytest

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

def test_count_lines_in_file():
    file_path = 'test.txt'
    with open(file_path, 'w') as file:
        file.write('Hello\nWorld\n')
    assert count_lines_in_file(file_path) == 2
    with open(file_path, 'w') as file:
        file.write('Hello\nWorld\n\n')
    assert count_lines_in_file(file_path) == 3
    with open(file_path, 'w') as file:
        file.write('')
    assert count_lines_in_file(file_path) == 0
```

**JavaScript (Jest)**
```javascript
const fs = require('fs');

function countLinesInFile(filePath) {
    return fs.readFileSync(filePath, 'utf8').split('\n').length;
}

describe('countLinesInFile', () => {
    it('should return 2 for a file with 2 lines', () => {
        const filePath = 'test.txt';
        fs.writeFileSync(filePath, 'Hello\nWorld\n');
        expect(countLinesInFile(filePath)).toBe(2);
    });

    it('should return 3 for a file with 3 lines', () => {
        const filePath = 'test.txt';
        fs.writeFileSync(filePath, 'Hello\nWorld\n\n');
        expect(countLinesInFile(filePath)).toBe(3);
    });

    it('should return 0 for a file with no lines', () => {
        const filePath = 'test.txt';
        fs.writeFileSync(filePath, '');
        expect(countLinesInFile(filePath)).toBe(0);
    });
});
```
