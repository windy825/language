### 1. 텝을 통해 자동 줄맞춤 하기 

```cpp
std::cout << "abc" << "\t" << "def" << std::endl;
std::cout << "ab" << "\t" << "cdef" << std::endl;

>>>
abc     def
ab      cdef
#공백 존재함
```



### 2. Using namespace

네임스페이스 등록, 자동 사용설정

```cpp
int main() 
{
	using namespace std;
    cout << "abc" << "\t" << "def" <<endl;
}
```



### 3. 오디오 출력하기

```cpp
int main()
{
	using namespace std;
    
    cout << "\a";
}
```



### 4. cin cout이 가지는 장점

printf 같은것과 달리 작성한 코드가, 파일 입출력 및 네트워크 입출력까지 다 커버 가능



### 5. 함수작성

```cpp
int addTwoNumbers(int num1, int num2)
{
	int sum = num1 + num2;
	return sum;
}
```

함수타입은 함수의 리턴값과 같이 맞춰줘야 한다.



### 6. rename 

![image-20230107220425833](https://user-images.githubusercontent.com/89068148/211153817-f57a5a31-ef1b-435f-911e-fadb74b0389b.png)



### 7. void 함수

리턴이 없는 함수 표시





### 8. reserved keyword

![image-20230107224110997](https://user-images.githubusercontent.com/89068148/211153819-07eca6b6-0143-40fc-8cbc-16e2c0e8e8fd.png)



### 9. main 함수의 작동

operating 시스템이 가장 먼저 찾는 함수임.

따라서 중복 선언시 에러, 그냥 reserved keyword처럼 여기면 된다.