import re

def replace_spelled_numbers(input_str):
    spelled_numbers = {
        'oneight': '18',
        'twone': '21',
        'sevenine': '79',
        'eightwo': '82',
        'eightthree': '83',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    for word, digit in spelled_numbers.items():
        input_str = input_str.replace(word, digit)
        input_str = input_str.replace(word.capitalize(), digit)

    return input_str

def parser():
    with open("./input.txt", "r") as outfile:
        data = outfile.readlines()
    for i in range(len(data)):
        data[i] = replace_spelled_numbers(data[i])
        data[i] = re.sub('\D', '', data[i])
    return data
    
def calibration(lines):
    for i in range(len(lines)):
        line = lines[i]
        if len(line) > 1:
            firstDigit = line[0]
            secondDigit = line[len(line) - 1]
            lines[i] = calibration_builder(firstDigit, secondDigit)
        else:
            firstDigit = line[0] 
            lines[i] = calibration_builder(firstDigit, firstDigit)
    return lines
        
def calibration_builder(value1, value2):
    tabOfValues = [value1, value2] 
    return int(''.join(tabOfValues))

def main():
    zebi = parser()
    result = calibration(zebi)
    value = 0
    for line in result:
        value = int(line) + value
    print(value)
    

if __name__ == "__main__":
    main()
            
        
    