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





## solution 생성 팁

- **`Create directory for solution`**

  한 솔루션안에 여러 프로젝트 생성시 유리

<br>

- Application type

  - **`Dynamic Link Library`, `Static Library`** 

    다른 프로그래머와 다른 프로젝트를 시작할때 기능을 제공하기 위함

  - **`Concole Application`**

    간단하게 콘솔창만 띄우고 하는 프로젝트

<br>

- Additional option

  - **`Precompiled Header`**

    소스파일이 굉장히 많은 큰 프로젝트의 경우 빌드 타임을 줄여주는 역할을 함.

    (그런데 의견이 분분함 옵션의 목적은 있으나 실효성은 애매함)

    멀티플랫폼 환경에선 쓰면 안된다. 리눅스에서 안 돌아간다.

- **`ctrl + shift + A` : source file,  add new item**

<br>

<br>

## Build

compile + linking 하는 과정, 결과물로 실행파일을 생성해준다.

- **`build > clean solution`** : 디버그 폴더 비우기
- **`ctrl + F5`** : start witout debuging 자동 빌드 및 실행
- **mode 의 차이**
  - debug mode : 실행속도 느리고, 용량 크다(디버그 관련 정보나 파일 포함)
  - release mode : 실행속도 빠르고, 용량 작다.

<br>

<br>

#### cmd 창 파일 탐색기

- **`d:`** : d 드라이브로 넘어감

- **`cd` + 파일 드래그 넣기** : 해당 파일 위치 이동

