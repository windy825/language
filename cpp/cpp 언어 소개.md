## C++ 

<br>

### 설계 철학

1. 프로그래머를 믿어라
2. 실제 세계에서 쓸모가 있어야 한다.
3. 프로그래머가 스스로 스타일을 선택할 수 있어야 한다.
4. 유용한 기능을 추가하는 것이 오용보다 더 중요하다.
5. 프로그래머의 의도를 알 수 없다면, 스스로 명시하게 한다.

<br>

### 프로그래밍 과정

<br>

#### 1. 문제 정의

<br>

#### 2. 해법 설계

<br>

#### 3. 구현 Write

<br>

#### 4. 컴파일 Compile

​	**- 윈도우 예시**

![image](https://user-images.githubusercontent.com/89068148/196169307-e73fd7a4-dbf7-4b15-8ea1-0e351bc2d745.png)

<br>

**- 리눅스의 경우**

```
// 명령어 예시
g++ -c file1.cpp file2.cpp file3.cpp

// g++ 리눅스 표준 컴파일러
```

<br>

#### 5. Linking

![image](https://user-images.githubusercontent.com/89068148/196170650-7d1a68ac-9f72-4285-8ed2-f04ecb998421.png)

- 오브젝트 파일들을 합치고 실행파일을 만드는 단계
- Runtime Support : 다른 프로그래머의 파일을 가져오는 것 (오픈소스 등)

<br>

#### 6. 테스트

- 테스트 진행 후 문제 발생시, 디버깅