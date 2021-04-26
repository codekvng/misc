#include <iostream>
#include <string>

using namespace std;

class Person {
	public:
		string name;
		int age;
		string hometown;
		string stays;
		void addYear() {
			age++;
		}
		void setGender(char pGender) {
			gender = pGender;
		}
		char getGender() {
			return gender;
		}
	private:
		char gender;
};

class Student : virtual public Person {
	public:
		void setSchoolName_Year(string sName, long int sYear) {
			schoolName = sName;
			year = sYear;
		}
		string getSchoolName() {
			return schoolName;
		}
		long int getYear() {
			return year;
		}
	private:
		string schoolName;
		long int year;
};

class Worker : virtual public Person {
	public:
		void setOrg_Year_Salary(string orgName, long int startYear, int orgSalary) {
			org = orgName;
			year = startYear;
			salary = orgSalary;
		}
		string getOrg() {
			return org;
		}
		long int getYear1() {
			return year;
		}
		int getSalary(){
			return salary;
		}

	private:
		string org;
		long int year;

	protected:
		int salary;
};

class StudentWorker : public Student, public Worker {
	public:
		string name;
		int age;
		string hometown;
		string stays;
		StudentWorker(string pName, int pAge) {
			name = pName;
			age = pAge;
		}
};

int main() {
  	//Objects go here
		return 0;
}
