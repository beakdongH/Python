import random
import time

word_list = ['안녕하세요',
             '안녕히가세요',
             '감사해요',
             '수고했어요',
             '도와줘요']

random.shuffle(word_list)
for i in word_list:
    s_time = time.time()
    user_input = str(input(i+'\n')).strip()
    e_time = time.time()-s_time

    correct = 0
    for index, c in enumerate(user_input):
        if index >= len(i):
            break
        if c == i[index]:
            correct+=1
    total_len = len(i)
    c = correct/total_len*100
    e = (total_len-correct)/total_len*100
    speed = correct / e_time*60
    print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".format(speed, c, e))