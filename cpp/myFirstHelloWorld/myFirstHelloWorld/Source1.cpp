#include <iostream>  
// # : ��ó���� preprocessor directive
// io : input,output

int main(void) // function�� Ư¡, ���ڸ� ���� �Ұ�ȣ�� ����
{
	int x; // ������ �����͸� ���� �޸� ���� x ����
	x = (1 + 2) * (3 + 4); // expression

	int y = x + 3;


	std::cout << y << std::endl;
	// std ���̺귯�� �̸��������� cout ���
	std::cout << 1 + 2 << std::endl;

	return 0; // statement ��ɹ�, ������ ���� ǥ���ϴ� ; �� �ʿ�
}

// main �� �����Ű�°� os��, �� �ڵ带 os���� �޸𸮸� ����ؼ� �̷���
// ������� �ּ��� �ǹ�