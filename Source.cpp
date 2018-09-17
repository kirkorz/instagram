#include<iostream>
using namespace std;

class CDate{
private:
	int Year, Month, Day;
public:
	void InputDate();
	void OutputDate();
	bool CheckDate();
	bool InspectLeapYear();

	CDate IncreaseYear();
	CDate IncreaseMonth();
	CDate IncreaseDay();
	CDate DecreaseYear();
	CDate DecreaseMonth();
	CDate DecreaseDay();

	CDate IncreaseYear(int n);
	CDate IncreaseMonth(int n);
	CDate IncreaseDay(int n);
	CDate DecreaseYear(int n);
	CDate DecreaseMonth(int n);
	CDate DecreaseDay(int n);

	int DayOrderInYear();
	string ConvertDay();
	int DeductdayToDay();
};

void CDate::InputDate(){
	cout << "Nhap ngay thang nam" << endl;
	cin >> this->Day >> this->Month >> this->Year;
}
void CDate::OutputDate(){
	cout << "Ngay :" << this->Day << endl;
	cout << "Thang :" << this->Day << endl;
	cout << "Nam :" << this->Day << endl;
}

void main(){
	CDate* tuan1 = new CDate;
	tuan1->InputDate();
	tuan1->OutputDate();

	
	printf("nothing");
	delete tuan1;
	system("pause");
}