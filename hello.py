#! /usr/bin/sh
# Python Program to demonstrate simple OOP

class Employee:

    def __init__(self, name, empID)->None:
        self._name = name
        self._empID = empID

    def getName(self)->str:
        return self._name

    def setName(self, name):
        self._name = name

    def getEmpID(self)->int:
        return self._empID

    def setEmpID(self, empID):
        self._empID = empID

    def __repr__(self):
        return f'{self._name} is employee with {self._empID} empID'

if __name__=='__main__':

    employee = Employee("Mulyo Santoso", 1101)

    print(employee.__repr__())
