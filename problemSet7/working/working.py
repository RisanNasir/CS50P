import re
import sys


def main():
    result = convert(input("Hours: ").strip())
    print(result)
    if result == "ValueError":
        sys.exit(1)
    else:
        sys.exit(0)

def convert(s):
    pattern = r'[01]?[0-9]:?[0-5]?[0-9]? AM to [01][0-9]?:?[0-5]?[0-9]? PM'
    pattern1 = r'([0-1]?[0-9]+):?([0-5][0-9])? (AM|PM) to ([0-1]?[0-9]):?([0-5][0-9])? (PM|AM)'

    match = re.search(pattern1, s)
    if  match:
        st_hr = (match.group(1))
        st_min = (match.group(2))
        stmidday = match.group(3)
        end_hr = (match.group(4))
        end_min = (match.group(5))
        endmidday = match.group(6)

        if stmidday == 'PM' and st_hr != '12':
            st_hr = int(st_hr) + 12
        elif stmidday == 'AM' and st_hr == '12':
            st_hr = int(0)
        else:
            st_hr = int(st_hr)

        if endmidday == 'PM' and end_hr != '12':
            end_hr = int(end_hr) + 12
        elif endmidday == 'AM' and end_hr == '12':
            end_hr = int(0)
        else:
            end_hr = int(end_hr)

        if st_min == None:
            st_min = 0
        if end_min == None:
            end_min = 0

        return (f'{st_hr:02}:{st_min:02} to {end_hr:02}:{end_min:02}')
    else:
            raise ValueError
            return 'ValueError'





if __name__ == "__main__":
    main()
