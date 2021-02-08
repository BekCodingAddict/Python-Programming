score=int(input("이번학기 성적을 입력하세용"))

if score>=90:
    print("A 학점을 받으셨습니다!")
else:
    if score>=80:
        print("B 학점을 받으셨습니다!")
    else:
        if score>=70:
            print("C 학점을 받으셨습니다!")
        else:
            if score>=60:
                print("D 학점을 받으셨습니다!")
            else:
                if score<60:
                    print("F 학점을 받으셨습니다!")