#include <iostream>  
// # : 전처리기 preprocessor directive
// io : input,output

int main(void) // function의 특징, 인자를 받을 소괄호가 있음
{
	int x; // 정수형 데이터를 받을 메모리 공간 x 선언
	x = (1 + 2) * (3 + 4); // expression

	int y = x + 3;


	std::cout << y << std::endl;
	// std 라이브러리 이름공간에서 cout 사용
	std::cout << 1 + 2 << std::endl;

	return 0; // statement 명령문, 문장의 끝을 표현하는 ; 가 필요
}

// main 을 실행시키는건 os임, 이 코드를 os님이 메모리를 사용해서 이렇게
// 실행시켜 주세요 의미