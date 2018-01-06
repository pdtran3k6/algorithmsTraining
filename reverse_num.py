import check
def reverse_num(num):
    new_num = 0
    while num > 0:
        next_digit = num % 10        
        num = num // 10     
        new_num = new_num * 10 + next_digit
    return new_num

check.expect("T1", reverse_num(1234), 4321)
check.expect("T2", reverse_num(6480039400000), 49300846)
check.expect("T3", reverse_num(71805126), 62150817)
    