import re

def parser():
    with open("./input.txt", "r") as outfile:
        data = outfile.readlines()
    data = [re.sub('\D', '', str) for str in data]
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
        print(line)
        value = int(line) + value
    print(value)
    

if __name__ == "__main__":
    main()
            
        
    