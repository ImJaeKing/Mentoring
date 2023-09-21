fi = open('input_data.txt','r')
file = fi.readlines()
print(f"input_data.txt 안에는 총 {len(file)}줄의 문자열이 들어 있었습니다.")
fi.close()

fo_list = []
for k in file:
    fo_list.append(k.strip().split())
print(fo_list)

fo = open('output_result.txt', 'w')

for i in file:
    values = i.split()
    body = int(values[0])
    tail = int(values[1])
    
    if body < 90 and tail > 11:
        fish = "salmon"
    else:
        fish = "carp"

    result = f"body: {body} tail: {tail} ==> {fish}\n"
    fo.write(result)

    print(result)

fi.close()
fo.close()